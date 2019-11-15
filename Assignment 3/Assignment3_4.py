No = int(input("How many elements you want into list : "))

List = []
cnt = 0

print("Enter elements into list")
for i in range(No):
	List.append(int(input()))

key = int(input("Enter key your want to search : "))

for i in List:
	if i == key:
		cnt += 1

print("The key ",key,"ocuures",cnt,"times.")