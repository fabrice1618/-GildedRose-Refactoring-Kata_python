# -*- coding: utf-8 -*-
import unittest

from Item import Item
from gilded_rose import GildedRose
from gilded_rose import AGED_BRIE, BACKSTAGE_PASS, SULFURAS

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_normal(self):
        items = [Item("normal", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("normal", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_normal_qualite_baisse_double(self):
        items = [Item("normal", 1, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 3):
            gilded_rose.update_quality()
            #print(items)
        self.assertEqual("normal", items[0].name)
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(5, items[0].quality)
        
    def test_aged_brie(self):
        items = [Item(AGED_BRIE, 5, 1)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 3):
            gilded_rose.update_quality()
        self.assertEqual(AGED_BRIE, items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_aged_brie_qualite_50(self):
        items = [Item(AGED_BRIE, 5, 48)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 3):
            gilded_rose.update_quality()
        self.assertEqual(AGED_BRIE, items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_pass(self):
        items = [Item(BACKSTAGE_PASS, 15, 1)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 2):
            gilded_rose.update_quality()
        self.assertEqual(BACKSTAGE_PASS, items[0].name)
        self.assertEqual(13, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_backstage_pass_inferieur_10(self):
        items = [Item(BACKSTAGE_PASS, 11, 1)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 3):
            gilded_rose.update_quality()
        self.assertEqual(BACKSTAGE_PASS, items[0].name)
        self.assertEqual(8, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_backstage_pass_inferieur_5(self):
        items = [Item(BACKSTAGE_PASS, 6, 1)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 3):
            gilded_rose.update_quality()
        self.assertEqual(BACKSTAGE_PASS, items[0].name)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_backstage_pass_sellin_inferieur0(self):
        items = [Item(BACKSTAGE_PASS, 1, 5)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 2):
            gilded_rose.update_quality()
        self.assertEqual(BACKSTAGE_PASS, items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_sulfuras(self):
        items = [Item(SULFURAS, 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(SULFURAS, items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras2(self):
        items = [Item(SULFURAS, 10, -20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(SULFURAS, items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(-20, items[0].quality)


if __name__ == '__main__':
    unittest.main()
