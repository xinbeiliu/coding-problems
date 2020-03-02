import unittest
import best_time_to_buy_and_sell_stock_I

class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        prices = [7,1,5,3,6,4]
        result = best_time_to_buy_and_sell_stock_I.maxProfit(prices)
        self.assertEqual(result, 5)

    def test_max_profit2(self):
        prices = []
        result = best_time_to_buy_and_sell_stock_I.maxProfit(prices)
        self.assertEqual(result, 0)

    def test_max_profit3(self):
        prices = [7, 6, 4, 3, 1]
        result = best_time_to_buy_and_sell_stock_I.maxProfit(prices)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()