"""
Given a range[L,R], print the sum of all the odd numbers within the range(inclusive of L and R).
Sample Testcase:
INPUT
5 10
OUTPUT
21
"""
b=input()
b=b.split(" ")
m=int(b[0])
n=int(b[1])
sum=0
for i in range(m,n+1):
    # print(i)
    if(i%2 != 0):
        sum=sum+i
print(sum)