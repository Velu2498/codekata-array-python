"""
Given a number N and an array of N strings, find the number of strings that are an anagram of 'kabali'.If there exists no anagram for the given string print '0'.
Input Size : 1 <= N <= 1000
Sample Testcase :
INPUT
5
kabali
kaabli
kababa
kab
kabail
OUTPUT
3
"""
n=int(input())
s=[]
c=0
for i in range(n):
    x=input()
    s.append(x)
k="kabali"
for j in range(n):
    if(sorted(s[j])==sorted(k)):
        c+=1
print(c)