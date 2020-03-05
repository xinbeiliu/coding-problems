# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    min_len = len(strs[0])
    for i in range(len(strs)):
        min_len = min(len(strs[i]), min_len)

    i = 0
    result = ""
    while i < min_len:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return result
        result += char
        i += 1
    return result