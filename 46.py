N=int(input())
m=map(int, input().split()[:N])
arr=[]
for i in m:
    if(i < N):
        arr.append(i)
if (len(arr)==0):
    print(-1)
else:
    arr.sort()
    arr=arr[::-1]
    print(" ".join(map(str,arr)))