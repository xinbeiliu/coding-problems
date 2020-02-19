# https://leetcode.com/problems/valid-anagram/

def valid_anagram(s, t):
    return sorted(s) == sorted(t)

print(valid_anagram("rat", "car"))


def valid_anagram_2(s, t):
    # check numbers of each char in a hashmap
    hash_map = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        hash_map[s[i]] = hash_map.get(s[i], 0) + 1
    print(hash_map)

    for j in range(len(t)):
        if t[j] not in hash_map:
            return False
        hash_map[t[j]] -= 1
        if hash_map[t[j]] < 0:
            return False
    return True


print(valid_anagram_2("aacc", "ccac"))

# O(n) - time complexity
# O(n) - space complexity