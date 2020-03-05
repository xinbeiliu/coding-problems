# https://leetcode.com/problems/count-and-say/

def countAndSay(n):

    if n == 1:
        return '1'

    prev = countAndSay(n - 1)
    res = ''
    ct = 1
    for i in range(len(prev)):
        if i == len(prev) - 1 or prev[i] != prev[i + 1]:
            res += str(ct) + prev[i]
            ct = 1
        else:
            ct += 1

    return res