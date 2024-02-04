from fastapi import FastAPI, Query
from pydanticModels import ApartmentSearchForm,ApartmentsObject ,ApartmentDetails
from typing import Dict
from sqlalchemy import create_engine, text
from db import SelectAllApartments,userFilter,insertNewApartmentToDB,newone


# FastAPI app instance
app = FastAPI()
@app.get("/")
async def check():

    return {"aprtments":"website"}

# Endpoint to get all apartment listings
@app.get("/listings")
async def get_listings():
    aprtments =SelectAllApartments()
    return aprtments

@app.get("/search")
async def getApartments(searchForm:ApartmentSearchForm):
    searchDict=searchForm.dict()
    getApartments=userFilter(searchDict)

    return getApartments


@app.post("/addnew")
async def addNewApartment(newApartments:ApartmentsObject):
    NewApartInfo=newApartments.dict()
    newListing=insertNewApartmentToDB(NewApartInfo)
    return newListing

