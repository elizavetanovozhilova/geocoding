from __future__ import annotations
from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        for trees in self.__data:
            full_address = self.search(area_id, trees)
            if full_address:
                final=', '.join([x.name for x in full_address])
                return final

    def search(self, area_id: str, tree: TreeNode) -> list:
        if tree.id == area_id:
            return [tree]
        else:
            for x in tree.areas:
                full_address = self.search(area_id, x)
                if full_address:
                    return [tree]+full_address

area = SimpleTreeGeocoder()
print(area._apply_geocoding('159'))
