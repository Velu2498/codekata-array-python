"""
Given a sentence S take out the extra spaces.If no extra space is present print the same as output.
Input Size : |s| <= 100000(complexity O(n))
Sample Testcase :
INPUT
codekata challenge
OUTPUT
codekata challenge
"""
S=input()
S=list(S)

for i in range(1,len(S)):
    if(S[i-1]==" " and S[i]==" "):
        S[i-1]=""
S="".join(S)
print(S)