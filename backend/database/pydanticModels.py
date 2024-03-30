from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Set, Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Text, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)

class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    year_built = Column(Integer)
    sqft = Column(Integer)
    beds = Column(Integer)
    bathrooms = Column(Integer)
    price_per_sqft = Column(Float)
    property_type = Column(String)
    garage = Column(Integer)
    HOA_fees = Column(Float)
    address = Column(Text)
    sqft_lot = Column(Integer)
    img_link = Column(Text)
    created_at = Column(DateTime, default=func.now())

class ApartmentInformation(BaseModel):
    address: str
    price: float
    year_built: int
    sqft: int
    beds: int
    bathrooms: int
    price_per_sqft: float
    property_type: str
    garage: int
    HOA_fees: int
    sqft_lot: int

class SignUpForm(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class PropertyType(str, Enum):
    single_family = "Single family"
    multi_family = "Townhome"
    condo = "condo"
    land = "Multi-Family"

class ApartmentSearchForm(BaseModel):
    min_price: float = None
    max_price: float = None
    min_year_built: int = None
    min_sqft: int = None
    max_sqft: int = None  
    min_beds: int = None
    max_beds: int = None 
    min_bathrooms: float = None
    max_bathrooms: float = None
    min_price_per_sqft: float = None
    property_type: Optional[Set[PropertyType]] = None  
    min_garage: int = None
    max_HOA_fees: float = None  
    address: str = None
    min_sqft_lot: int = None
    
class SignUpForm(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class SignInRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

def convert_to_apartment_response(apartment: Apartment) -> ApartmentInformation:
    return ApartmentInformation(
        price=apartment.price,
        year_built=apartment.year_built,
        sqft=apartment.sqft,
        beds=apartment.beds,
        bathrooms=apartment.bathrooms,
        price_per_sqft=apartment.price_per_sqft if apartment.price_per_sqft is not None else 0.0,
        property_type=apartment.property_type,
        garage=apartment.garage,
        HOA_fees=apartment.HOA_fees,
        address=apartment.address,
        sqft_lot=apartment.sqft_lot,
    )