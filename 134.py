"""
Given a number N and an array of N elements,sort the array in increasing order and print the original indices of the elements present in sorted array.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
5 4 3 2 1
OUTPUT
5 4 3 2 1
"""
n=int(input())
b=map(int,input().split()[:n])
b=list(b)
c=list(b)
c.sort()
ans=[]
# print(" ".join(map(str,c)))
for i in range(len(b)):
    for j in range(len(c)):
        if(b[i]==c[j]):
            ans.append(j+1)
print(" ".join(map(str,ans)))
