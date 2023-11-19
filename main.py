import random

from fabrics.gold_generator import GoldGenerator
from fabrics.gem_generator import GemGenerator
from fabrics.silver_generator import SilverGenerator
from fabrics.sword_generator import SwordGenerator
from fabrics.shield_generator import ShieldGenerator
from fabrics.bow_generator import BowGenerator
from fabrics.armor_generator import ArmorGenerator
from fabrics.spell_generator import SpellGenerator


if __name__ == '__main__':

    ''' Вариант с созданием списка из генераторов каждого типа, число которых соответствует пропорции '''

    # generators = [GemGenerator()]
    # generators.extend([GoldGenerator() for i in range(3)])
    # generators.extend([SwordGenerator() for i in range(10)])
    # generators.extend([ShieldGenerator() for i in range(10)])
    # generators.extend([BowGenerator() for i in range(10)])
    # generators.extend([ArmorGenerator() for i in range(10)])
    # generators.extend([SpellGenerator() for i in range(10)])
    # for i in range(10):
    #     generators[random.randint(0, len(generators) - 1)].create_item().open()

    ''' Вариант с изменением количества возвращающихся экземпляров в каждом генераторе '''

    generators = [SwordGenerator(), ShieldGenerator(), BowGenerator(), ArmorGenerator(), SpellGenerator(),
                  GoldGenerator(), GemGenerator()]

    for i in range(2):
        generator = generators[random.randint(0, len(generators) - 1)]
        for item in generator.create_item():
            item.open()
