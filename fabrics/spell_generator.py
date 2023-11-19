from fabrics.item_fabric import ItemFabric
from products.spell import Spell


class SpellGenerator(ItemFabric):
    def create_item(self):
        return [Spell() for i in range(10)]

        # return Spell()
