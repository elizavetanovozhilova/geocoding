from __future__ import annotations
from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.areas_dict={}
        self.tree_dict(self.__data)

    def tree_dict(self, tree: list[TreeNode], parent: str='') -> dict:
        for area in tree:
            if parent:
                full_address=f'{parent}, {area.name}'
            else:
                full_address=area.name
            self.areas_dict[area.id]=full_address
            self.tree_dict(area.areas, full_address)


    def _apply_geocoding(self, area_id: str) -> str:
        return self.areas_dict.get(str(area_id))


area=MemorizedTreeGeocoder()
print(area._apply_geocoding('98'))