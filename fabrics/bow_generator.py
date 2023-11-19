from fabrics.item_fabric import ItemFabric
from products.bow import Bow


class BowGenerator(ItemFabric):
    def create_item(self):
        return [Bow() for i in range(10)]

        # return Bow()
