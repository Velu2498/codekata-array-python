"""
Check whether the given 4 points form a square or not.
Example:
INPUT
10 10
10 20
20 20
20 10
OUTPUT
yes

"""

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
if (x1==x2 and x3==x4 and y1==y4 and y2==y3):
												print("yes")
else:
	print("no")
  