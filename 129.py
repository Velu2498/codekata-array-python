"""
Given a binary number convert it to hexadecimal.
Sample Testcase :
INPUT
1100100
OUTPUT
64
"""
n=input()
b=int(n,2)
print(hex(b).replace("0x",""))
	