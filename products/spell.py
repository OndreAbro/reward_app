from products.game_item import GameItem


class Spell(GameItem):
    def open(self):
        print('SPELL')
