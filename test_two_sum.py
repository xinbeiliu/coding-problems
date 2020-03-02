import unittest
import two_sum

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        '''test with target can be added
           from the number in the arr'''
        arr = [2,5,5,11]
        target = 10
        result = two_sum.two_sum(arr, target)
        self.assertEqual(result, [1,2])

    def test_two_sum2(self):
        '''test with target can't be added from
            any number in the arr'''
        arr = [2,5,6,11]
        target = 10
        result = two_sum.two_sum(arr, target)
        self.assertEqual(result, None)

    def test_two_sum3(self):
        '''test with empty arr'''
        arr = []
        target = 10
        result = two_sum.two_sum(arr, target)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()