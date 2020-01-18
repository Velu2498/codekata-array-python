"""
Given 2 numbers N,X and an array of N elements, check if there exists any 2 numbers in the array with sum equal to X.If found print 'yes' otherwise print 'no'
Input Size : N,X <= 100000
Sample Testcase :
INPUT
4 4
2 2 0 0
OUTPUT
yes
"""

N,X=map(int,input().split())
m=map(int, input().split()[:N])
m=list(m)
count=0
for i in range(len(m)):
    for j in range(len(m)):
        if (i!=j):
            if (m[i]+m[j]==X):
                # print("yes")
                count+=1
                break
            
if(count!=0):
    print("yes")
else:
    print("no")