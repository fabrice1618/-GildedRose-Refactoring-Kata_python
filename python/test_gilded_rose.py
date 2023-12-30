# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from gilded_rose import AGED_BRIE, BACKSTAGE_PASS, SULFURAS, CONJURED


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_normal(self):
        items = [Item("Clavier azerty", 4, 11)]
        attendus = [
            {'sell_in': 3, 'quality': 10},
            {'sell_in': 2, 'quality': 9},
            {'sell_in': 1, 'quality': 8},
            {'sell_in': 0, 'quality': 7},
            {'sell_in': -1, 'quality': 5},
            {'sell_in': -2, 'quality': 3},
            {'sell_in': -3, 'quality': 1},
            {'sell_in': -4, 'quality': 0},
            {'sell_in': -5, 'quality': 0},
            {'sell_in': -6, 'quality': 0},
        ]
        gilded_rose = GildedRose(items)
        for attendu in attendus:
            gilded_rose.update_quality()

            self.assertEqual("Clavier azerty", items[0].name)
            self.assertEqual(attendu['sell_in'], items[0].sell_in)
            self.assertEqual(attendu['quality'], items[0].quality)


    def test_aged_brie(self):
        items = [Item(AGED_BRIE, 4, 0)]
        attendus = [
            {'sell_in': 3, 'quality': 1},
            {'sell_in': 2, 'quality': 2},
            {'sell_in': 1, 'quality': 3},
            {'sell_in': 0, 'quality': 4},
            {'sell_in': -1, 'quality': 6},
            {'sell_in': -2, 'quality': 8},
        ]
        gilded_rose = GildedRose(items)
        for attendu in attendus:
            gilded_rose.update_quality()

            self.assertEqual(AGED_BRIE, items[0].name)
            self.assertEqual(attendu['sell_in'], items[0].sell_in)
            self.assertEqual(attendu['quality'], items[0].quality)

    def test_sulfuras(self):
        items = [Item(SULFURAS, 0, 80)]
        gilded_rose = GildedRose(items)
        for _ in range(0, 10):
            gilded_rose.update_quality()

        self.assertEqual(SULFURAS, items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


    def test_backstage_pass(self):
        items = [Item(BACKSTAGE_PASS, 15, 20)]
        attendus = [
            {'sell_in': 14, 'quality': 21},
            {'sell_in': 13, 'quality': 22},
            {'sell_in': 12, 'quality': 23},
            {'sell_in': 11, 'quality': 24},
            {'sell_in': 10, 'quality': 25},
            {'sell_in': 9, 'quality': 27},
            {'sell_in': 8, 'quality': 29},
            {'sell_in': 7, 'quality': 31},
            {'sell_in': 6, 'quality': 33},
            {'sell_in': 5, 'quality': 35},
            {'sell_in': 4, 'quality': 38},
            {'sell_in': 3, 'quality': 41},
            {'sell_in': 2, 'quality': 44},
            {'sell_in': 1, 'quality': 47},
            {'sell_in': 0, 'quality': 50},
            {'sell_in': -1, 'quality': 0},
            {'sell_in': -2, 'quality': 0},
        ]
        gilded_rose = GildedRose(items)
        for attendu in attendus:
            gilded_rose.update_quality()

            self.assertEqual(BACKSTAGE_PASS, items[0].name)
            self.assertEqual(attendu['sell_in'], items[0].sell_in)
            self.assertEqual(attendu['quality'], items[0].quality)

    def test_backstage_pass2(self):
        items = [Item(BACKSTAGE_PASS, 5, 49)]
        attendus = [
            {'sell_in': 4, 'quality': 50},
            {'sell_in': 3, 'quality': 50},
            {'sell_in': 2, 'quality': 50},
            {'sell_in': 1, 'quality': 50},
            {'sell_in': 0, 'quality': 50},
            {'sell_in': -1, 'quality': 0},
            {'sell_in': -2, 'quality': 0},
        ]
        gilded_rose = GildedRose(items)
        for attendu in attendus:
            gilded_rose.update_quality()

            self.assertEqual(BACKSTAGE_PASS, items[0].name)
            self.assertEqual(attendu['sell_in'], items[0].sell_in)
            self.assertEqual(attendu['quality'], items[0].quality)

    def test_conjured(self):
        items = [Item(CONJURED, 3, 6)]
        attendus = [
            {'sell_in': 2, 'quality': 5},
            {'sell_in': 1, 'quality': 4},
            {'sell_in': 0, 'quality': 3},
            {'sell_in': -1, 'quality': 1},
            {'sell_in': -2, 'quality': 0},
            {'sell_in': -3, 'quality': 0},
            {'sell_in': -4, 'quality': 0},
        ]
        gilded_rose = GildedRose(items)
        for attendu in attendus:
            gilded_rose.update_quality()

            self.assertEqual(CONJURED, items[0].name)
            self.assertEqual(attendu['sell_in'], items[0].sell_in)
            self.assertEqual(attendu['quality'], items[0].quality)


if __name__ == '__main__':
    unittest.main()
