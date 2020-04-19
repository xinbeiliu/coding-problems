# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# 9
# 10 20 20 10 10 30 50 10 20
# output 3

def sockMerchant(n, ar):
    hash_map = {}
    counter = 0
    for num in ar:
        hash_map[num] = hash_map.get(num, 0) + 1
    for key, value in hash_map.items():
        if value != 1:
            counter += value // 2
    return counter