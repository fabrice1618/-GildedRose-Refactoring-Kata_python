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

# Modifier quality et vérifier que 0 <= quality <= 50
def quality_add(item, val):
    result = item.quality + val
    result = 50 if result > 50 else result
    result = 0 if result < 0 else result
    item.quality = result

def update_aged_brie(item):
    # Logique de mise à jour pour Aged Brie
    quality_add(item, 1)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        quality_add(item, 1)

def update_backstage_passes(item):
    # Logique de mise à jour pour Backstage Passes
    if item.sell_in < 6:
        quality_add(item, 3)
    elif item.sell_in < 11:
        quality_add(item, 2)
    else:
        quality_add(item, 1)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.quality = 0

def update_sulfuras(item):
    # Logique de mise à jour pour Sulfuras
    pass

def update_conjured(item):
    # Logique de mise à jour pour Conjured
    quality_add(item, -1)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        quality_add(item, -1)

def update_normal_item(item):
    # Logique de mise à jour pour les autres articles
    quality_add(item, -1)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        quality_add(item, -1)

# Appeler la fonction de mise à jour en fonction du type d'article
def update(item):
    if item.name == AGED_BRIE:
        update_aged_brie(item)
    elif item.name == BACKSTAGE_PASS:
        update_backstage_passes(item)
    elif item.name == SULFURAS:
        update_sulfuras(item)
    elif item.name == CONJURED:
        update_conjured(item)
    else:
        update_normal_item(item)

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update(item)


