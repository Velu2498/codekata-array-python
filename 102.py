"""
Given a number N, followed by an array of N elements,print 'yes' if it is a sorted array otherwise print 'no'.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
3
2 3 7
OUTPUT
yes
"""
n=int(input())
l=list(map(int,input().split()[:n]))
k=[]
for i in range(len(l)):
    k.append(l[i])
k.sort()
if(l==k):
    print("yes")
else:
    print("no")
