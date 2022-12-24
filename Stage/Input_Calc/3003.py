chess_input = list(map(int, input().split()))
chess_set = [1,1,2,2,2,8]

print(*[y-x for x,y in zip(chess_input,chess_set)])