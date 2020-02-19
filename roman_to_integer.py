# https://leetcode.com/problems/roman-to-integer/

def roman_to_int(s):

    hash_map = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}

    # IV, IX, XL, XC, CD, CM - subtraction
    result = 0
    for i in range(0, len(s) - 1):
        if hash_map[s[i]] < hash_map[s[i + 1]]:
            result -= hash_map[s[i]]
        else:
            result += hash_map[s[i]]
    return result + hash_map[s[-1]]
