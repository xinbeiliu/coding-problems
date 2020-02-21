# https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balanced_string_split(s):
    result = 0
    counter = 0

    for i in range(len(s)):
        if s[i] == 'L':
            counter += 1
        elif s[i] == 'R':
            counter -= 1
        if counter == 0:
            result += 1

    return result

print(balanced_string_split('RLRRLLRLRL'))