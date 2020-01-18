"""
Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
Input Size : N <= 100000
Sample Testcase :
INPUT
2143
OUTPUT
1 3
"""
s=int(input())
v=[]
new=[]
sum=0
while(s > 0):
    n=s%10
    v.append(n)
    s=s//10
v=v[::-1]
for i in range(len(v)):
    val=int(v[i])
    if(val%2 != 0):
        new.append(val)
        sum+=1
if(sum==0):
    print(-1)
else:
    print(" ".join(map(str,new)))