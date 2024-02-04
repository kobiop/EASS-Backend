from fastapi import FastAPI
from src.models.pydanticModels import ApartmentSearchForm,ApartmentsObject
from src.db.db import SelectAllApartments,userFilter,insertNewApartmentToDB


app = FastAPI()
@app.get("/")
async def check():

    return {"aprtments":"website"}

@app.get("/listings")
async def get_listings():
    aprtments =SelectAllApartments()

    return aprtments

@app.post("/search")
async def getApartments(searchForm:ApartmentSearchForm):
    searchDict=searchForm.dict()
    getApartments=userFilter(searchDict)

    return getApartments

@app.post("/addnew")
async def addNewApartment(newApartments:ApartmentsObject):
    NewApartInfo=newApartments.dict()
    newListing=insertNewApartmentToDB(NewApartInfo)

    return newListing

