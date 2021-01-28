from .connections import Mongo

class IncidentService:

    def __init__(self, **kwargs):
        self.collection = 'incidents'

    def add_incident(self, incident):
        # TODO: Validate incident
        with Mongo() as db:
            collect = db[self.collection]
            if not collect.find_one(incident):
                collect.insert_one(incident)

    def query_incident(self, query):
        with Mongo() as db:
            collect = db[self.collection]
            return collect.find_one(query, {'_id': 0})

    def query_incidents(self, query):
        print(query)
        with Mongo() as db:
            collect = db[self.collection]
            return list(collect.find(query, {'_id': 0}))

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