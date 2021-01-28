from datetime import datetime, timedelta
# TODO: Maybe use multiple weather apis/libraries incase one is down or has breaking changes.
from meteostat import Stations, Daily, Hourly
# disable cache for now
Stations.max_age = 0
Daily.max_age = 0
Hourly.max_age = 0

class WeatherService:
    """Class that provides weather data for certain locations and times."""
    def __init__(self, **kwargs):
        # Location
        lat = kwargs.get('latitude')
        lng = kwargs.get('longitude')
        if lat and lng:
            self.location = {'latitude': lat, 'longitude': lng}
        # Should country and state override lat and lng ?
        country = kwargs.get('country')
        state = kwargs.get('state')
        if country and state:
            self.location = {'country': country, 'state': state}
        # Time Period
        # TODO: Validate start < end
        self.start = kwargs.get('start')
        self.end = kwargs.get('end')
        # Stations
        self.granularity = kwargs.get('granularity', 'hourly')
        self._stations = Stations()
        if kwargs.get('auto_load', False):
            self.set_stations()

    @property
    def location(self):
        return getattr(self, '_location', None)

    @location.setter
    def location(self, loc):
        # Set location
        if not isinstance(loc, dict):
            raise Exception('Location must be a dictionary.')
        # Only set (lat, long) or (country, state).
        if  loc.get('latitude') and loc.get('longitude'):
            # TODO: Type check
            self._location = {'latitude': loc['latitude'], 'longitude': loc['longitude']}
        elif  loc.get('country') and loc.get('state'):
            # TODO: Type Check
            self._location = {'country': loc['country'], 'state': loc['state']}
        else:
            raise Exception(f"Location did not have correct format. Expected dict with 'latitude' and 'longitude' or 'country' and 'state' but received {loc}")

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        if isinstance(start, datetime):
            self._start = start
        elif start:
            try:
                self._start = datetime.strptime(start, "%Y-%m-%d")
            except ValueError:
                raise Exception(f"Start date: {start}, does not follow the format: YYYY-MM-DD.")
        else:
            self._start = datetime.today() - timedelta(days = 1)

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if isinstance(end, datetime):
            self._end = end
        elif end:
            try:
                self._end = datetime.strptime(end, "%Y-%m-%d")
            except ValueError:
                raise Exception(f"End date: {end}, does not follow the format: YYYY-MM-DD.")
        else:
            self._end = datetime.today()

    @property
    def granularity(self):
        return self._granularity

    @granularity.setter
    def granularity(self, gran):
        if not isinstance(gran, str):
            raise TypeError(" Granularity must be a string")
        elif gran not in ['daily', 'hourly']:
            raise Exception("Granularity must be either 'daily' or 'hourly'.")
        else:
            self._granularity = gran

    @property
    def station(self):
        return self._station

    @station.setter
    def station(self, station_number):
        if not isinstance(station_number, int):
            raise TypeError("Station must be a integer id")
        self._station = self._stations.fetch(station_number)

    def get_stations(self):
        return self._stations

    def set_stations(self, location=None):
        if location:
            self.location = location
        loc = self.location
        if  loc.get('latitude') and loc.get('longitude'):
            self._stations = self._stations.nearby(loc['latitude'], loc['longitude'])
        elif  loc.get('country') and loc.get('state'):
            self._stations = self._stations.region(loc['country'], loc['state'])
        self._stations = self._stations.inventory(self.granularity, (self.start, self.end))
        # Auto set station to first result
        self.station = 1

    def get_daily_data(self):
        data = Daily(self.station, self.start, self.end)
        return data.fetch()

    def get_hourly_data(self):
        data = Hourly(self.station, self.start, self.end)
        return data.fetch()
    