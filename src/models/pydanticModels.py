from pydantic import BaseModel, Field
from enum import Enum
from typing import Set, Optional

class ApartmentDetails(BaseModel):
    id : int = Field(default=1)
    price: float = Field(default=0.0)
    year_built: int = Field(default=0)
    sqft: int = Field(default=0)
    beds: int = Field(default=0)
    bathrooms: int = Field(default=0)
    price_per_sqft: float = Field(default=0.0)
    property_type: str = Field(default="")
    garage: int = Field(default=0)
    HOA_fees: float = Field(default=0.0)
    address: str = Field(default="No Adress")
    sqft_lot: int = Field(default=0)
    img_link: str = Field(default="No Pic")
    created_at: str = Field(default="No Date")


class ApartmentsObject(BaseModel):
    price: float
    year_built: int
    sqft: int
    beds: int
    bathrooms: int
    property_type: str
    garage: int
    HOA_fees: float
    address: str
    sqft_lot: int
    img_link: str



class PropertyType(str, Enum):
    house = "house"
    apartment = "apartment"
    condo = "condo"
    townhouse = "townhouse"

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
    property_type: Optional[Set[PropertyType]] = None  # Allow a set of PropertyType or None
    min_garage: int = None
    max_HOA_fees: float = None  # Adjust as needed
    address: str = None
    min_sqft_lot: int = None
