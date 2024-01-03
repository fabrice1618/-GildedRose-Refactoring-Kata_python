# -*- coding: utf-8 -*-

from Item import Item

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedItem(Item):
    def __init__(self, item):
        self.item = item

        if self.item.name == AGED_BRIE:
            self.update_method = self.update_aged_brie
        elif item.name == BACKSTAGE_PASS:
            self.update_method = self.update_backstage_pass
        elif item.name == SULFURAS:
            self.update_method = self.update_sulfuras
        else:
            self.update_method = self.update_normal

    def update(self):
        self.update_method()

    def update_aged_brie(self):
        self.quality_add(1)
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.quality_add(1)

    def update_sulfuras(self):
        pass

    def update_backstage_pass(self):
        self.quality_add(self.quality_increase_backstage_pass())
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0

    def quality_increase_backstage_pass(self):
        quality_increase = 0
        if 0 <= self.item.sell_in < 6:
            quality_increase = 3
        if 6 <= self.item.sell_in < 11:
            quality_increase = 2
        if self.item.sell_in >= 11:
            quality_increase = 1
        return quality_increase
    
    def update_normal(self):
        self.quality_add(-1)
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.quality_add(-1)        

    def quality_add(self, val):
        result = self.item.quality + val
        result = 50 if result > 50 else result
        result = 0 if result < 0 else result
        self.item.quality = result

    def __repr__(self):
        return f"Gilded Item: ({self.item.name=}, {self.item.sell_in=}, {self.item.quality=})" 

class GildedRose(object):

    def __init__(self, items):
        self.items = [GildedItem(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update()
