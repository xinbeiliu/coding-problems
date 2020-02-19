# https://leetcode.com/problems/valid-palindrome/

def valid_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


print(valid_palindrome("Marge, let's \"went.\" I await news telegram."))

print(valid_palindrome("race a car"))

# O(2n) - time complexity
# O(n) - space complexity