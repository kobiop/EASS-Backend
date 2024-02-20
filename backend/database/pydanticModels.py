from pydantic import BaseModel
from enum import Enum
from typing import Set, Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Text, DateTime
from sqlalchemy.sql import func

Base = declarative_base()
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

class ApartmentAdd(BaseModel):
    price: float
    year_built: int
    sqft: int
    beds: int
    bathrooms: int
    price_per_sqft: float
    property_type: str
    garage: int
    HOA_fees: float
    address: str
    sqft_lot: int
    img_link: str

class PropertyType(str, Enum):
    single_family = "Single family"
    multi_family = "Multi-Family"
    condo = "condo"
    land = "Land"
    apartment = "apartment"
    house = "house"

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
