# Given a string, find the
# first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

def firstUniqChar(s):

    hash_map = {}
    for i in range(len(s)):
        hash_map[s[i]] = hash_map.get(s[i],0) + 1

    for j in range(len(s)):
        if hash_map[s[j]] == 1:
            return j

    return -1

print(firstUniqChar('leetcode'))