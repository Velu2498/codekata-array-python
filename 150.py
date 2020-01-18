"""
Given a number N, print all the prime factors once in ascending order.
Input Size : N <= 100000
Sample Testcase :
INPUT
100
OUTPUT
2 5
"""

n=int(input())
ans=[]
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            # print(i)
            ans.append(i)
    i=i+1
print(" ".join(map(str,ans)))