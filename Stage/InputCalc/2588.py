input = list(map(int, input().split()))

output_6 = input[0]*input[1]

output_3 = input[0]*(input[1]%10)
input[1] = input[1]//10

output_4 = input[0]*(input[1]%10)
input[1] = input[1]//10

output_5 = input[0]*input[1]


print(output_3, output_4, output_5, output_6, sep='\n')