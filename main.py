from fastapi import FastAPI
from src.models.pydanticModels import ApartmentSearchForm, ApartmentsObject
from src.db.db import get_all_apartments, filter_apartments_by_user, insert_new_apartment

app = FastAPI()

@app.get("/")
async def health_check():
    return {"apartments": "website"}

@app.get("/listings")
async def get_listings():
    apartments = get_all_apartments()
    return apartments

@app.post("/search")
async def get_apartments(search_form: ApartmentSearchForm):
    search_dict = search_form.dict()
    filtered_apartments = filter_apartments_by_user(search_dict)
    return filtered_apartments

@app.post("/addnew")
async def add_new_apartment(new_apartment: ApartmentsObject):
    new_apart_info = new_apartment.dict()
    new_listing = insert_new_apartment(new_apart_info)
    return new_listing
