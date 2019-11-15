no = int(input("Enter number : "))
rem = 0
add = 0

while no > 0:
	rem = no % 10
	no = no // 10
	add = add + rem

print(add)