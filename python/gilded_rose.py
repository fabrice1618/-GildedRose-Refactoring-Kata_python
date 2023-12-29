# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Pre sell_in
            if item.name == AGED_BRIE:
                if item.quality < 50:
                    item.quality = item.quality + 1

            if item.name == BACKSTAGE_PASS:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1

            if item.name == SULFURAS:
                pass

            if item.name != AGED_BRIE and item.name != BACKSTAGE_PASS and item.name != SULFURAS:
                if item.quality > 0:
                    item.quality = item.quality - 1

            # Update sell_in
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            # Post sell_in
            if item.sell_in < 0:
                if item.name == AGED_BRIE:
                    if item.quality < 50:
                        item.quality = item.quality + 1

                if item.name == BACKSTAGE_PASS:
                    item.quality = item.quality - item.quality

                if item.name == SULFURAS:
                    pass

                if item.name != AGED_BRIE and item.name != BACKSTAGE_PASS and item.name != SULFURAS:
                    if item.quality > 0:
                        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
