# https://leetcode.com/problems/factorial-trailing-zeroes/

# 1! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120 - one trailing zero
# 6! = 6*5*4*3*2*1 = 720 - one trailing zero
# 7! = 7*6*5*4*3*2*1 = 5040 - two trailing zeros
# how many multiples of 5 in a given n?

import math
def trailing_zero(n):
    if n < 5:
        return 0
    if n < 10:
        return 1

    return math.floor(n/5 + trailing_zero(n/5))

print(trailing_zero(100))

def trailing_zero_2(n):
    result = 0
    while n > 0:
        result += math.floor(n/5)
    n /= 5

print(trailing_zero(101))