# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

def quality_sub(quality, val):
    result = quality - val
    return result if result >= 0 else 0

def quality_add(quality, val):
    result = quality + val
    return result if result <= 50 else 50

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update(item)

    def update(self, item):
        if item.name == AGED_BRIE:
            self.update_aged_brie(item)
        elif item.name == BACKSTAGE_PASS:
            self.update_backstage_passes(item)
        elif item.name == SULFURAS:
            self.update_sulfuras(item)
        elif item.name == CONJURED:
            self.update_conjured(item)
        else:
            self.update_normal_item(item)

    def update_aged_brie(self, item):
        # Logique de mise à jour pour Aged Brie
        item.quality = quality_add(item.quality, 1)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = quality_add(item.quality, 1)

    def update_backstage_passes(self, item):
        # Logique de mise à jour pour Backstage Passes
        item.quality = quality_add(item.quality, 1)
        if item.sell_in < 11:
            item.quality = quality_add(item.quality, 1)
        if item.sell_in < 6:
            item.quality = quality_add(item.quality, 1)

        item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
            item.quality = 0

    def update_sulfuras(self, item):
        # Logique de mise à jour pour Sulfuras
        pass

    def update_conjured(self, item):
        # Logique de mise à jour pour Conjured
        item.quality = quality_sub(item.quality, 1)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = quality_sub(item.quality, 1)

    def update_normal_item(self, item):
        # Logique de mise à jour pour les autres articles
        item.quality = quality_sub(item.quality, 1)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = quality_sub(item.quality, 1)

