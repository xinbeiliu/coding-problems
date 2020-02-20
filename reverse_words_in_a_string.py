# https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverse_words(s):

    result = []
    for word in s.split():
        word = word[::-1]
        result.append(word)

    return ' '.join(result)

print(reverse_words('Let\'s take LeetCode contest'))