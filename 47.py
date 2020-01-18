N,K=map(int,input().split())
s=map(int, input().split()[:N])
s=list(s)
arr=[]
dis={}
# print(K)
for i in s:
    count=0
    for j in s:
        if(i==j):
            count+=1
            dis[i]=count
key=dis.keys()
for i in key:
    if(dis[i]==K):
        # print(i)
        arr.append(i)

if(len(arr)==0):
    print(-1)
else:
    arr.sort()
    print(" ".join(map(str,arr)))

    
    




