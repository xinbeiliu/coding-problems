# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

def snail(input):
    result = []
    top_row_idx = 0
    bottom_row_idx = len(input)-1 #2
    left_col_idx = 0
    right_col_idx = len(input[0])-1 #2

    while top_row_idx <= bottom_row_idx and left_col_idx <= right_col_idx:
        # top row traversal
        for i in range(left_col_idx, right_col_idx+1):
            result.append(input[top_row_idx][i])
        top_row_idx += 1

        # right col traversal
        for j in range(top_row_idx, bottom_row_idx+1):
            result.append(input[j][right_col_idx])
        right_col_idx -= 1

        # bottom row traversal
        for k in range(right_col_idx, left_col_idx-1, -1):
            result.append(input[bottom_row_idx][k])
        bottom_row_idx -= 1

        # left col traversal
        for l in range(bottom_row_idx, top_row_idx-1, -1):
            result.append(input[l][left_col_idx])
        left_col_idx += 1

    return result

print(snail([[1,2,3],
             [4,5,6],
             [7,8,9]]))