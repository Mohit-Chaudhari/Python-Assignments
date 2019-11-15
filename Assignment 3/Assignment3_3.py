No = int(input("How many elements you want into list : "))

List = []

print("Enter elements into list : ")
for i in range(No):
	List.append(int(input()))

print("Minimum number from given list is",min(List))