"""
A number is given as input. Find the odd digits in the number, add them and find if the sum is odd or not. If even print E, if odd print O.
Input Size : N <= 10000000000
Sample Testcase :
INPUT
413
OUTPUT
E
"""

n=int(input())
# print(n.split())
arr=[]
sum=0
while(n>0):
    d=n%10
    arr.append(d)
    n=int(n/10)
# print(arr)
for i in arr:
    if(i%2 != 0):
        sum=sum+i
if(sum%2==0):
    print("E")
else:
    print("O")