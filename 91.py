"""
Given a string S consisting of only '(' and ')', print 'yes' if it is balanced otherwise print 'no'.
Sample Testcase :
INPUT
(())
OUTPUT
yes
""" 
s=input()
s1=0
s2=0
for i in range(len(s)):
    if(s[i]=="("):
        s1+=1
    elif(s[i]==")"):
        s2+=1
    else:
        print("no")
if(s1==s2):
    print("yes")
else:
    print("no")