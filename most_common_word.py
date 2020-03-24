# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case
# sensitive.  The answer is in lowercase.

# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"

import collections

def most_common_word(paragraph, banned):

    for char in "!?',;.":
        paragraph = paragraph.replace(char, " ")

    hash_map = collections.Counter(paragraph.lower().split())

    res = ''
    count = 0

    for k, v in hash_map.items():
        if v > count and k not in banned:
            count = v
            res = k

    return res

print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit."), ["hit"])