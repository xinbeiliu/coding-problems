# https://leetcode.com/problems/repeated-substring-pattern/

def repeated_substring(s):

    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return True
    return False

print(repeated_substring('ababab'))
print(repeated_substring(('abc')))