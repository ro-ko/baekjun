import sys
        
N = int(sys.stdin.readline().strip())

div = 2
while N!=1:  # N과m을 나눴을때 몫이 1이 되면 멈춤.
  if N%div==0: 
    print(div) 
    N = N//div
  else:
    div += 1