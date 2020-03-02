import unittest
import reverse_a_string

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = ["H","a","n","n","a","h"]
        result = reverse_a_string.reverse_str(s)
        self.assertEqual(result, ["h","a","n","n","a","H"])

if __name__ == '__main__':
    unittest.main()