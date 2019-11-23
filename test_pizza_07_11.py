import unittest
from pizza import Pizza, PIZZA_BIG_SIZE, PIZZA_SMALL_SIZE


class TestPizza(unittest.TestCase):

    # def setUp(self):
    #     self.pizza = (PIZZA_BIG_SIZE)
    #     self.pizza = (PIZZA_SMALL_SIZE)

    def test_small_pizza(self):
        pizza = Pizza(PIZZA_SMALL_SIZE)
        self.assertEqual(pizza.size, 0)

    def test_big_pizza(self):
        pizza = Pizza(PIZZA_BIG_SIZE)
        self.assertEqual(pizza.size, 1)

    def test_wrong_pizza_size(self):
        with self.assertRaises(TypeError):
            Pizza(4)

    if __name__ == '__main__':
        unittest.main()

