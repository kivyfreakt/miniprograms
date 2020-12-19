def is_safe_pos(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False

    i = row
    j = col
    while(i >= 0 and j>= 0):
        if(board[i][j]):
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while(i < n and j>= 0):
        if(board[i][j]):
            return False
        i += 1
        j -= 1
    return True



def find_pos(n, board, col):
    if (col >= n):
        return True
    for row in range(n):
        if is_safe_pos(board, row, col):
            board[row][col] = 1
            if (find_pos(n, board, col+1)):
                return True
            board[row][col] = 0

    return False


n = int(input())
board = [[0]*n for i in range(n)]
check = find_pos(n, board, 0)
if check:
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print("")
else:
    print(-1)
