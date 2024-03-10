from __future__ import  annotations
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
        for tree in self.__data:
            res = self._find_area(tree, area_id)
            if res:
                return ', '.join([i.name for i in res])

    def _find_area(self, tree: TreeNode, area_id: str):
        if tree.id == area_id:
            return [tree]
        for node in tree.areas:
            res = self._find_area(node, area_id)
            if res:
                return [tree, *res]

r=SimpleTreeGeocoder()
r._apply_geocoding('88')