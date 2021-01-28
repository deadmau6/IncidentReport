from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Address(BaseModel):
    city: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    number: Optional[int] = Field(None)
    geohash: Optional[str] = Field(None)
    first_due: Optional[int] = Field(None)
    latitude: Optional[float] = Field(None)
    address_id: Optional[str] = Field(None)
    longitude: Optional[float] = Field(None)
    postal_code: Optional[int] = Field(None)
    cross_street1: Optional[str] = Field(None)
    address_line1: Optional[str] = Field(None)
    response_zone: Optional[int] = Field(None)
    cross_street2: Optional[str] = Field(None)
    suffix_direction: Optional[str] = Field(None)
    prefix_direction: Optional[str] = Field(None)
    common_place_name: Optional[str] = Field(None)

class ExtendedData(BaseModel):
    dispatch_duration: Optional[int] = Field(None)
    event_duration: Optional[int] = Field(None)
    response_time: Optional[int] = Field(None)

class Description(BaseModel):
    type: Optional[str] = Field(None)
    subtype: Optional[str] = Field(None)
    event_id: Optional[int] = Field(None)
    day_of_week: Optional[str] = Field(None)
    hour_of_day: Optional[int] = Field(None)
    incident_number: Optional[str] = Field(None)
    event_closed: Optional[datetime] = Field(None)
    event_opened: Optional[datetime] = Field(None)
    #extended_data: Optional[ExtendedData] = Field(None)
    loi_search_complete: Optional[datetime] =  Field(None)
    first_unit_arrived: Optional[datetime] =  Field(None)
    first_unit_enroute: Optional[datetime] =  Field(None)
    first_unit_dispatched: Optional[datetime] =  Field(None)
