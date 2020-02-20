# https://leetcode.com/problems/goat-latin/

def to_goat_latin(S):
    result = []
    for word in S.split():
        if word[0] in 'aeiouAEIOU':
            word += 'ma'
        else:
            word = word[1:] + word[0] + 'ma'
        result.append(word)

    for i in range(len(result)):
        result[i] += (i + 1) * 'a'

    return ' '.join(result)


print(to_goat_latin("I speak Goat Latin"))