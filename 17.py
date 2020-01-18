"""
Given a string S, print 2 strings such that first string containing all characters in odd position(s) and other containing all characters in even position(s).
Sample Testcase :
INPUT
XCODE
OUTPUT
XOE CD
"""

v=input()
o=[]
e=[]
for i in  range(len(v)):
    if(i%2==0):
        e.append(v[i])
    else:
        o.append(v[i])
e="".join(e)
o="".join(o)
print(e,o)