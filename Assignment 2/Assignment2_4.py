No = int(input("Enter number : "))
Add = 0

for i in range(1,No):
	if No % i == 0:
		Add = Add + i

print("\nSummation of factorial is",Add)