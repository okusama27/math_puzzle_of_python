import unittest


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEquals(10, product.amount)
        product = five.times(3)
        self.assertEquals(15, product.amount)

    def test_equality(self):
        self.assertTrue(Dollar(5).__eq__(Dollar(5)))
        self.assertFalse(Dollar(5).__eq__(Dollar(6)))


class Dollar:

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # self.amount *= multiplier
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount


if __name__ == '__main__':
    test = MoneyTest()
    test.test_multiplication()