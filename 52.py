"""
Given a number N followed by N elements for every 2 consecutive numbers print the maximum of the 2.
Input Size : N <= 100000 (ie do it in O(n) time complexity)
Sample Testcase :
INPUT
5
1 1 3 0 5
OUTPUT
1 3 3 5
"""

n=int(input())
b=map(int,input().split()[:n])
b=list(b)
ans=[]

for i in range(len(b)-1):
    if(b[i]>b[i+1]):
        # print(b[i])
        ans.append(b[i])
    else:
        # print(b[i+1])
        ans.append(b[i+1])
ans=" ".join(map(str,ans))
print(ans)