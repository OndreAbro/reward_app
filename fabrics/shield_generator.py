from fabrics.item_fabric import ItemFabric
from products.shield import Shield


class ShieldGenerator(ItemFabric):
    def create_item(self):
        return [Shield() for i in range(10)]

        # return Shield()
