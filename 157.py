"""
Given a number N and array of N integers, print the prefix sum array for each position if it is divisible by 2 else print the element itself.
Input Size : N <= 10000
Sample Testcase :
INPUT
4
2 4 4 4
OUTPUT
2 6 10 14
"""
n=int(input())
a=map(int,input().split()[:n])
a=list(a)
c=a[0]
l=[]
l.append(a[0])
for i in range(1,n):
    c=c+a[i]
    if(c%2==0):
        l.append(c)
    else:
        l.append(a[i])
l=" ".join(map(str,l))
print(l)