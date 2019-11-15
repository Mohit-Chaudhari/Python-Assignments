no = int(input("Enter number : "))

cnt = 0

while no>0:
	no = no//10
	cnt = cnt + 1

print("Count is",cnt)