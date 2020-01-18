"""
Given a string S,count the maximum number of times a character repeated in the string.If no character is repeated print '0'.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
codekata
OUTPUT
2
"""
s=input()
s=list(s)
arr=[]
dis={}
for i in s:
    count=0
    for j in s:
        if(i==j):
            count+=1
            dis[i]=count
print(dis)
key=dis.keys()
for i in key:
    arr.append(dis[i])
# print(arr)
print(max(arr)) 