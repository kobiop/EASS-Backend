from fastapi import FastAPI,HTTPException
from src.models.pydanticModels import ApartmentSearchForm,ApartmentAdd
from src.db.db import get_all_apartments, filter_apartments_by_user, insert_new_apartment,bring_last

app = FastAPI()

@app.get("/")
async def health_check():
    return {"server":"up"}

@app.get("/listings")
async def get_listings():
    try:
        apartments = get_all_apartments()
        return {"apartments": apartments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    

@app.post("/search")
async def get_apartments(search_form: ApartmentSearchForm):
    try:
        search_dict = search_form.dict()
        filtered_apartments = filter_apartments_by_user(search_dict)
        return filtered_apartments
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@app.post("/addnew")
async def add_new_apartment(new_apartment: ApartmentAdd):
    try:
        new_apart_info = new_apartment.dict()
        new_listing = insert_new_apartment(new_apart_info)
        return {"new_listing": new_listing}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")    
    
