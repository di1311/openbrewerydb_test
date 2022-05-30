from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state: str
    county_province: Optional[str]
    postal_code: str
    country: str
    longitude: Optional[str]
    latitude: Optional[str]
    phone: Optional[str]
    website_url: Optional[HttpUrl]
    updated_at: str
    created_at: str


class AutocompleteBrewery(BaseModel):
    id: str
    name: str


class ListOfBreweries(BaseModel):
    __root__: List[Brewery]


class AutocompleteBreweries(BaseModel):
    __root__: List[AutocompleteBrewery]
