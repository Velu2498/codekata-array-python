"""
Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3
"""
j=input()
a=input().split()
#a=list(a)
l=len(a)
n=[]
last=a[l-1]
if(l%2==0):
    for i in range(1,l+1,2):
        n.append(a[i])
        n.append(a[i-1])
    n=" ".join(map(str,n))
    print(n)
else:
    for i in range(1,l,2):
        n.append(a[i])
        n.append(a[i-1])
    n.append(last)
    n=" ".join(map(str,n))
    print(n)