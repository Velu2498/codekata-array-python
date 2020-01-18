"""
Given a string S, print the reverse of the string after removing the vowels.If the resulting string is empty print '-1'.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
codekata
OUTPUT
tkdc
"""
N=int(input())
S=input()
vow=["a",'e','i','o','u']
l=[]
i=len(S)-1

while(i>-1):
    l.append(S[i])
    i=i-1

for j in range(len(l)):
    for k in range(len(vow)):
        if(vow[k]==l[j]):
            l[j]=""
print("".join(l))