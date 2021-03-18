import json


class Yacht:
    def __init__(self, name=None, waterline_length=None, width=None, precipitation=None,
                 water_displacement=None, engine=None, sleeping_places=None, water_tank_volume=None, length=None,
                 fuel_tank_volume=None, total_sailing_area=None, genoa=None, front_photo_url=None, side_photo_url=None):
        self.uuid = None
        self.side_photo_url = side_photo_url
        self.front_photo_url = front_photo_url
        self.total_sailing_area = total_sailing_area
        self.genoa = genoa
        self.fuel_tank_volume = fuel_tank_volume
        self.water_tank_volume = water_tank_volume
        self.sleeping_places = sleeping_places
        self.engine = engine
        self.precipitation = precipitation
        self.water_displacement = water_displacement
        self.width = width
        self.waterline_length = waterline_length
        self.length = length
        self.name = name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
