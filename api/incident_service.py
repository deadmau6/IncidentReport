from .connections import Mongo
from .weather_service import WeatherService
from datetime import timedelta
import json

class IncidentService:

    def __init__(self, **kwargs):
        self.weather = WeatherService()
        self.collection = 'incidents'

    def add_incident(self, incident):
        # TODO: Validate incident
        with Mongo() as db:
            collect = db[self.collection]
            if not collect.find_one(incident):
                collect.insert_one(incident)

    def enrich_data(self, data):
        if data is None:
            return None
        # Set time frame based on event opening and closing.
        self.weather.start = data['description']['event_opened']
        self.weather.end = data['description']['event_closed']
        # Check that there is at least one hour of data.
        diff = self.weather.end - self.weather.start
        if diff.total_seconds() < 3600:
            self.weather.end = self.weather.end + timedelta(hours=1)
        # Get the location and set the nearest station.
        loc = {'latitude': data['address']['latitude'], 'longitude': data['address']['longitude']}
        self.weather.set_stations(loc)
        # Get the station information.
        station_info = self.weather.station
        weather_info = self.weather.get_hourly_data()
        data['weather'] = {}
        data['weather']['station'] = station_info.to_dict()
        data['weather']['dataframe'] = json.loads(weather_info.to_json())
        return data


    def query_incident(self, query):
        with Mongo() as db:
            collect = db[self.collection]
            data = collect.find_one(query, {'_id': 0})
        return self.enrich_data(data)

    def query_incidents(self, query):
        with Mongo() as db:
            collect = db[self.collection]
            res = list(collect.find(query, {'_id': 0}))
        if len(res) == 0:
            return None
        return [self.enrich_data(entry) for entry in res]

    @staticmethod
    def address_query_builder(*args):
        feild_names = [
        'city',
        'name',
        'type',
        'state',
        'number',
        'geohash',
        'first_due',
        'latitude',
        'address_id',
        'longitude',
        'postal_code',
        'cross_street1',
        'address_line1',
        'response_zone',
        'cross_street2',
        'suffix_direction',
        'prefix_direction',
        'common_place_name'
        ]
        query = {}
        for k, v in zip(feild_names, args):
            if v:
                query[f"address.{k}"] = v
        return query

    @staticmethod
    def description_query_builder(*args):
        feild_names = [
        'type',
        'subtype',
        'event_id',
        'day_of_week',
        'hour_of_day',
        'incident_number',
        'event_closed',
        'event_opened',
        'dispatch_duration',
        'event_duration',
        'response_time',
        'loi_search_complete',
        'first_unit_arrived',
        'first_unit_enroute',
        'first_unit_dispatched'
        ]
        query = {}
        for k, v in zip(feild_names, args):
            if v and k in ['dispatch_duration', 'event_duration','response_time']:
                query[f'description.extended_data.{k}'] = v
            elif v:
                query[f'description.{k}'] = v
        return query