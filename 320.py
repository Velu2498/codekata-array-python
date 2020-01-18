"""
Alternate sorting:Given a number N followed by array of N elements,sort the array in such a way that the first number is the first maximum and second number is the 1st minimum 3rd number isthe 2nd maximum and so on.
Input Size : N <= 100000
Sample Testcase :
INPUT
8
7 623 19 10 11 9 3 15
OUTPUT
623 3 19 7 15 9 11 10 
"""
k = int(input())
n=list(map(int,input().split()[:k]))
l=len(n)
n.sort(reverse = True)
y=[]
h=l//2
last=n[h]
for i in range(h):
    y.append(n[i])
    y.append(n[-i-1])
if(l%2==1):
    y.append(last)
y= " ".join(map(str,y))
print(y)