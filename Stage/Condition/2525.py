start = list(map(int,input().split()))
time = int(input())

if(start[1]+time<60): print(start[0],start[1]+time)
elif(start[0]+(start[1]+time)//60>23): print(start[0]+(start[1]+time)//60-24, (start[1]+time)%60)
else: print(start[0]+(start[1]+time)//60, (start[1]+time)%60)