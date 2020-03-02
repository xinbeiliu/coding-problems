# https://leetcode.com/problems/implement-strstr/

def strStr(haystack, needle):

    L = len(haystack)
    n = len(needle)

    for i in range(L):
        if haystack[i:n+i] == needle:
            return i

    return -1

print(strStr('hello', 'll'))