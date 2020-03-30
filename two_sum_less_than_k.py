# Given an array A of integers and integer K, return the maximum S such that there exists
# i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation:
# We can use 34 and 24 to sum 58 which is less than 60.

def two_sum(A, K):
    A = sorted(A)
    res = []
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] < K:
                res.append(A[i] + A[j])

    if len(res) == 0:
        return -1
    else:
        return max(res)

print(two_sum([34,23,1,24,75,33,54,8], 60))