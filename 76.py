"""
Given a number N and an array of N elements, every number is repeated except for one. Print that one number.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
10
1 2 3 2 3 3 2 5 5 2
OUTPUT
1
"""
n=int(input())
b=map(int,input().split()[:n])
b=list(b)
dist={}
for i in b:
    count=0
    for j in b:
        if(i==j):
            count+=1
            dist[i]=count
e=dist.keys()
# print(e)
for i in e:
    # print(i)
    if(dist[i]==1):
        print(i)