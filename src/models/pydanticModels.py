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

from pydantic import BaseModel, Field

class ApartmentsObject(BaseModel):
    price: float = Field(..., description="Price")
    year_built: int = Field(..., description="Year built")
    sqft: int = Field(..., description="Square footage")
    beds: int = Field(..., description="Number of bedrooms")
    bathrooms: int = Field(..., description="Number of bathrooms")
    property_type: str = Field(..., description="Property type")
    garage: int = Field(..., description="Number of garage spaces")
    HOA_fees: float = Field(..., description="HOA fees")
    address: str = Field(..., description="Address")
    sqft_lot: int = Field(..., description="Square footage of the lot")
    img_link: str = Field(..., description="Image link")


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
