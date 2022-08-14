height = []
sum = 0
for i in range(9):
    x = int(input())
    height.append(x)
    sum = sum+x

rest = sum-100
breaker = False

for i in range(8):
    for j in range(i+1,9):
        if height[i]+height[j]==rest:
            num1 = height[i]
            num2 = height[j]
            height.remove(num1)
            height.remove(num2)
            breaker = True
            break
    if breaker==True:
        break

height.sort()
for i in height:
    print(i)