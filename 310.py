"""
Given a number N, Print sum of every didgit to the power of the weight of corresponding digit(Explanation : If the input is 12345 and then output calculated as (1^0)+(2^1)+(3^2)+(4^3)+(5^4)).
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
100
OUTPUT
1
"""
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