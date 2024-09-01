input = list(map(int, input().split()))

print((input[0]+input[1])%input[2], ((input[0]%input[2]) + (input[1]%input[2]))%input[2], (input[0]*input[1])%input[2], ((input[0]%input[2])*(input[1]%input[2]))%input[2],sep='\n')