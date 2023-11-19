from fabrics.item_fabric import ItemFabric
from products.sword import Sword


class SwordGenerator(ItemFabric):
    def create_item(self):
        return [Sword() for i in range(10)]

        # return Sword()
