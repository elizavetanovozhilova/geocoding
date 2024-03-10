from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        area=API.get_area(area_id)
        full_address=[area.name]
        while area.parent_id:
            area=API.get_area(area.parent_id)
            full_address.append(area.name)

        return ', '.join(full_address)

r=SimpleQueryGeocoder()
print(r._apply_geocoding('88'))

