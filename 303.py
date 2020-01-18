"""
Given a number N, print the sum of squares of all its digits.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
12
OUTPUT
5
"""
m=int(input())
m=str(m)
v=0
for i in range(len(m)):
    v=v+int(m[i])**2
print(v)