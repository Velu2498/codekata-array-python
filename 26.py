"""
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes
"""
N,K=map(int, input().split())
V=map(int, input().split()[:N])
for i in V:
	if(i==K):
            print("yes")
            break
else:
    print("no")