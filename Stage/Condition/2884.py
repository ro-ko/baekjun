time = list(map(int,input().split()))

if (time[1]-45 >= 0): print(time[0],time[1]-45)
elif(time[1]-45 < 0)&(time[0]==0): print(23,time[1]+15)
else: print(time[0]-1,time[1]+15)