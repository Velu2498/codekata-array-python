"""
Given an array, find the maximum difference between any two elements.
Input Size : N <= 1000000(complexity O(n) or O(nlogn))
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
4
"""
s=int(input())
l=list(map(int,input().split()[:s]))
l.sort()
ll=len(l)
print(l[ll-1]-l[0])