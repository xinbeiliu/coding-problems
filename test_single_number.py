import unittest
import single_number

class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        arr = [2,2,1]
        result = single_number.single_number(arr)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()