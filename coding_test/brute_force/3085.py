def check():
    row_cnt, col_cnt, row_max, col_max = 1,1,1,1
    for i in range(size):
        for j in range(size-1):
            if board[i][j] == board[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_max, row_cnt)
        row_cnt = 1
    for j in range(size):
        for i in range(size-1):
            if board[i][j] == board[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_max, col_cnt)
        col_cnt = 1
    return max(row_max, col_max)


size = int(input())
board = [list(input()) for i in range(size)]
ans = 0
ans = check()

direction = [[-1,0],[1,0],[0,1],[0,-1]]

for row in range(size):
    for col in range(size):
        for dir in direction:
            x = row + dir[0]
            y = col + dir[1]
            if x<0 or x>=size or y<0 or y>=size:
                continue
            if board[row][col] != board[x][y]:
                board[x][y], board[row][col] = board[row][col], board[x][y]
                ans = max(ans, check())
                board[x][y], board[row][col] = board[row][col], board[x][y]
print(ans)