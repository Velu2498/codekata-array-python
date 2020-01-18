# q.no:510 on process
n=int(input())
c=[]
cs=[]
math=[]
eng=[]
for i in range(n):
    b=input().split()
    b=list(b)
    c.append(b)
# print(c) 
for i in range(len(c)):
    cs.append(c[i][1])
    math.append(c[i][2])
    eng.append(c[i][3])
# print(cs,math,eng)


# q.no:52
# n=int(input())
# b=map(int,input().split()[:n])
# b=list(b)
# ans=[]

# for i in range(len(b)-1):
#     if(b[i]>b[i+1]):
#         # print(b[i])
#         ans.append(b[i])
#     else:
#         # print(b[i+1])
#         ans.append(b[i+1])
# ans=" ".join(map(str,ans))
# print(ans)


# q.n0:126
# b=input()
# b=b.split(" ")
# m=int(b[0])
# n=int(b[1])
# sum=0
# for i in range(m,n+1):
#     # print(i)
#     if(i%2 != 0):
#         sum=sum+i
# print(sum)


# q.no:76
# n=int(input())
# b=map(int,input().split()[:n])
# b=list(b)
# dist={}
# for i in b:
#     count=0
#     for j in b:
#         if(i==j):
#             count+=1
#             dist[i]=count
# e=dist.keys()
# # print(e)
# for i in e:
#     # print(i)
#     if(dist[i]==1):
#         print(i)


# q.no:150
# n=int(input())
# ans=[]
# i=1
# while(i<=n):
#     k=0
#     if(n%i==0):
#         j=1
#         while(j<=i):
#             if(i%j==0):
#                 k=k+1
#             j=j+1
#         if(k==2):
#             # print(i)
#             ans.append(i)
#     i=i+1
# print(" ".join(map(str,ans)))


# q.no:134
# n=int(input())
# b=map(int,input().split()[:n])
# b=list(b)
# c=list(b)
# c.sort()
# ans=[]
# # print(" ".join(map(str,c)))
# for i in range(len(b)):
#     for j in range(len(c)):
#         if(b[i]==c[j]):
#             ans.append(j+1)
# print(" ".join(map(str,ans)))


# q.no:158
# n=int(input())
# # print(n.split())
# arr=[]
# sum=0
# while(n>0):
#     d=n%10
#     arr.append(d)
#     n=int(n/10)
# # print(arr)
# for i in arr:
#     if(i%2 != 0):
#         sum=sum+i
# if(sum%2==0):
#     print("E")
# else:
#     print("O")


# q.no:47
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


# q.no:42
# N,X=map(int,input().split())
# m=map(int, input().split()[:N])
# m=list(m)
# count=0
# for i in range(len(m)):
#     for j in range(len(m)):
#         if (i!=j):
#             if (m[i]+m[j]==X):
#                 # print("yes")
#                 count+=1
#                 break
            
# if(count!=0):
#     print("yes")
# else:
#     print("no")


# q.no:46
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

# q.no:513
# n=int(input())
# b=map(int,input().split()[:n])
# b=list(b)
# b.sort()
# print(b[0]+b[1])

# q.no:310
s=int(input())
v=[]
sum=0
while(s > 0):
    n=s%10
    v.append(n)
    s=s//10
v=v[::-1]
for i in range(len(v)):
    val=int(v[i])
    sum=sum+(val**i)
print(sum)



