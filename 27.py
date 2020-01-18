"""
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
"""

n,m=map(int,input().split())
b=map(int,input().split()[:n])
b=list(b)
count=-1
for i in b:
    if(i==m):
        count+=1
print(count)