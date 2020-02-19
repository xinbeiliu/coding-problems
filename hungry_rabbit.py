

def hungry_rabbit(garden):
    if len(garden) == 0 or len(garden[0]) == 0:
        return 0

    garden_1 = [g_row[:] for g_row in garden]

    rows = [len(garden) // 2, len(garden) // 2]
    if len(garden) % 2 == 0:
        rows[0] -= 1

    cols = [len(garden[0]) // 2, len(garden[0]) // 2]
    if len(garden[0]) % 2 == 0:
        cols[0] -= 1

    max = 0
    row = -1
    col = -1

    for r in rows:
        for c in cols:
            if garden[r][c] > max:
                max = garden[r][c]
                row = r
                col = c

    if row < 0 or col < 0:
        return 0

    return hungry_rabbit_recur(garden_1, row, col)


def hungry_rabbit_recur(garden, row, col):
    max_carrot = 0
    next_col = -1
    next_row = -1

    for r, c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if row + r >= 0 and row + r < len(garden) and \
                col + c >= 0 and col + c < len(garden[row]):
            if garden[row + r][col + c] > max_carrot:
                max_carrot = garden[row + r][col + c]
                next_col = col + c
                next_row = row + r

    carrots = garden[row][col]
    garden[row][col] = 0

    if max_carrot > 0 and next_row >= 0 and next_col >= 0:
        carrots += hungry_rabbit_recur(garden, next_row, next_col)

    return carrots


if __name__ == "__main__":
    garden = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]
    ]

    print(hungry_rabbit(garden))