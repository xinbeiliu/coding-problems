# You are given a license key represented as a string S which consists only alphanumeric
# character and dashes. The string is separated into N+1 groups by N dashes.
#
# Given a number K, we would want to reformat the strings such that each group contains
# exactly K characters, except for the first group which could be shorter than K, but still
# must contain at least one character. Furthermore, there must be a dash inserted between
# two groups and all lowercase letters should be converted to uppercase.
#
# Given a non-empty string S and a number K, format the string according to the rules
# described above.

# Input: S = "5F3Z-2e-9-w", K = 4
#
# Output: "5F3Z-2E9W"
#
# Explanation: The string S has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.

# Input: S = "2-5g-3-J", K = 2
#
# Output: "2-5G-3J"
#
# Explanation: The string S has been split into three parts, each part has 2 characters
# except the first part as it could be shorter as mentioned above.

def license_key_formatting(S, K):
    res = []
    S = S.replace('-', '').upper()
    rem = len(S) % K
    if rem != 0:
        res.append(S[:rem])
    for i in range(rem, len(S), K):
        res.append(S[i:i+K])

    return ('-').join(res)

print(license_key_formatting('2-5g-3J', 2))