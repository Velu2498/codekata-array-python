
"""
Iron Man wants to extract an infinity stone from a safe. The safe is protected by a password and Iron Man knows the clue to the password which is “sum one and two when sorted they are true”. Decode the clue from the test case and help Iron Man open the safe.

 

Input Description:
Size of the array followed by the elements of the array

Output Description:
Sum of 2 specific elements in the array.

Sample Input :
5
9 8 3 2 1

Sample Output :
3
"""
n=int(input())
b=map(int,input().split()[:n])
b=list(b)
b.sort()
print(b[0]+b[1])