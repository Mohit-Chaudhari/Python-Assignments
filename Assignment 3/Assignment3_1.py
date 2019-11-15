No = int(input("Enter number of elements : "))
List1 = []

print("Enter elements : ")
for i in range(No):
	List1.append(int(input()))

print("Sum is ",sum(List1))