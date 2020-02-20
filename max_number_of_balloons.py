# https://leetcode.com/problems/maximum-number-of-balloons/

def max_number_of_balloons(text):
    return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))

print(max_number_of_balloons('nlaebolko'))