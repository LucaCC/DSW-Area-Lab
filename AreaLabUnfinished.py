import math
import unittest


def circleArea(radius):
    """Return the area of a circle"""
    return math.pi * radius * radius


def rectArea(base, height):
    return base * height


def trapArea(base1, base2, height):
    return ((base1 + base2) / 2) * height


def triArea(base, height):
    return (base * height) / 2


class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25 * math.pi)
    """def testRectArea(self):

    def testTrapArea(self):

    def testTriArea(self):"""
