from fabrics.item_fabric import ItemFabric
from products.armor import Armor


class ArmorGenerator(ItemFabric):
    def create_item(self):
        return [Armor() for i in range(10)]

        # return Armor()
