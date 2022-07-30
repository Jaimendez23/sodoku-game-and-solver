


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1,10):
        if valid(bo, x, (row, col)):
            bo[row][col] = x
            if solve(bo):
                return True
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for x in range(len(bo[0])):
        if bo[pos[0]][x] == num and pos[1] != x:
            return False
    # check column
    for x in range(len(bo[0])):
        if bo[x][pos[1]] == num and pos[0] != x:
            return False

    # check Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True



def print_board(bo):
    for x in range(len(bo)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[x][j])
            else:
                print(str(bo[x][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


print_board(board)
print("   ")
solve(board)
print("   ")
print_board(board)
