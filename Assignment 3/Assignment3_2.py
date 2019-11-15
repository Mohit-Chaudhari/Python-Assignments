No = int(input("How many elements you want into list : "))

List = []

print("Enter elements : ")
for i in range(No):
	List.append(int(input()))

print("Maximum element from list is ",max(List))