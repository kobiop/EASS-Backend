from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database.db import get_all_apartments, filter_apartments_by_user, insert_new_apartment
from database.pydanticModels import ApartmentInformation, ApartmentSearchForm
from auth import auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    try:
        return {"server": "up"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/listings")
async def get_listings():
    try:
        apartments = get_all_apartments()
        return {"listings": apartments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/search", response_model=list[ApartmentInformation])
async def get_apartments_according_user_pref(search_form: ApartmentSearchForm):
    try:
        search_dict = search_form.dict()
        filtered_apartments = filter_apartments_by_user(search_dict)
        return filtered_apartments
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/add-listing", response_model=ApartmentInformation)
async def add_new_apartment(new_apartment: ApartmentInformation):
    try:
        new_apart_info = new_apartment.dict()
        new_listing = insert_new_apartment(new_apart_info)
        return new_listing
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
app.include_router(auth_router, prefix="/auth")