from pydantic import BaseModel
from typing import List, Optional

class ActivityBase(BaseModel):
    name: str
    description: Optional[str] = None

class TransferBase(BaseModel):
    from_location: str
    to_location: str
    mode: str

class HotelBase(BaseModel):
    name: str
    location: str

class ItineraryDayBase(BaseModel):
    day_number: int

class Activity(ActivityBase):
    class Config:
        orm_mode = True

class Transfer(TransferBase):
    class Config:
        orm_mode = True

class Hotel(HotelBase):
    class Config:
        orm_mode = True

class ItineraryDay(ItineraryDayBase):
    hotel: Hotel
    transfers: List[Transfer] = []
    activities: List[Activity] = []

    class Config:
        orm_mode = True

class ItineraryBase(BaseModel):
    name: str
    nights: int

class ItineraryCreate(ItineraryBase):
    pass

class ItineraryOut(ItineraryBase):
    id: int
    days: List[ItineraryDay] = []

    class Config:
        orm_mode = True
