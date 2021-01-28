from typing import Optional
from fastapi import APIRouter, Query, HTTPException
from datetime import datetime
from .query_model import Address, Description
from .incident_service import IncidentService

router = APIRouter()

@router.get("/incident/{incident_number}")
async def query_incident_by_id(incident_number: str):
    query = {'description.incident_number': incident_number}
    service = IncidentService()
    result = service.query_incident(query)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Could not find Incident with id {incident_number}")
    return result

@router.post("/incidents/")
async def query_incidents(description: Optional[Description] = None, address: Optional[Address] = None):
    query = {}
    if description:
        description = description.dict()
        for k, v in description.items():
            if v:
                query[f"description.{k}"] = v
    if address:
        address = address.dict()
        for k, v in address.items():
            if v:
                query[f"address.{k}"] = v
    service = IncidentService()
    results = service.query_incidents(query)
    if results is None:
        raise HTTPException(status_code=404, detail=f"Could not find Incident with query: {query}")
    return {'results': results}

@router.get("/incidents/address/")
async def query_incidents_by_address(
    city: Optional[str] = Query(None),
    name: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
    number: Optional[int] = Query(None),
    geohash: Optional[str] = Query(None),
    first_due: Optional[int] = Query(None),
    latitude: Optional[float] = Query(None),
    address_id: Optional[str] = Query(None),
    longitude: Optional[float] = Query(None),
    postal_code: Optional[int] = Query(None),
    cross_street1: Optional[str] = Query(None),
    address_line1: Optional[str] = Query(None),
    response_zone: Optional[int] = Query(None),
    cross_street2: Optional[str] = Query(None),
    suffix_direction: Optional[str] = Query(None),
    prefix_direction: Optional[str] = Query(None),
    common_place_name: Optional[str] = Query(None)
    ):
    query = IncidentService.address_query_builder(
        city,
        name,
        type,
        state,
        number,
        geohash,
        first_due,
        latitude,
        address_id,
        longitude,
        postal_code,
        cross_street1,
        address_line1,
        response_zone,
        cross_street2,
        suffix_direction,
        prefix_direction,
        common_place_name)
    service = IncidentService()
    results = service.query_incidents(query)
    if results is None:
        raise HTTPException(status_code=404, detail=f"Could not find Incident with address query: {query}")
    return {'results': results}

@router.get("/incidents/description/")
async def query_incidents_by_description(
    type: Optional[str] = Query(None),
    subtype: Optional[str] = Query(None),
    event_id: Optional[int] = Query(None),
    day_of_week: Optional[str] = Query(None),
    hour_of_day: Optional[int] = Query(None),
    incident_number: Optional[str] = Query(None),
    event_closed: Optional[datetime] = Query(None),
    event_opened: Optional[datetime] = Query(None),
    dispatch_duration: Optional[int] = Query(None),
    event_duration: Optional[int] = Query(None),
    response_time: Optional[int] = Query(None),
    loi_search_complete: Optional[datetime] =  Query(None),
    first_unit_arrived: Optional[datetime] =  Query(None),
    first_unit_enroute: Optional[datetime] =  Query(None),
    first_unit_dispatched: Optional[datetime] =  Query(None)
    ):
    # Construct Query object
    query = IncidentService.description_query_builder(
        type,
        subtype,
        event_id,
        day_of_week,
        hour_of_day,
        incident_number,
        event_closed,
        event_opened,
        dispatch_duration,
        event_duration,
        response_time,
        loi_search_complete,
        first_unit_arrived,
        first_unit_enroute,
        first_unit_dispatched)
    # Get results
    service = IncidentService()
    results = service.query_incidents(query)
    if results is None:
        raise HTTPException(status_code=404, detail=f"Could not find Incident with description query: {query}")
    return {'results': results}