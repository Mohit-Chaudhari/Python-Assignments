import functools

No = int(input("HOw many elements : "))

List = []

print("Enter elements : ", end="")
for i in range(No):
	List.append(int(input()))

List = list(filter(lambda x: x % 2 == 0, List))

List = list(map(lambda x : x * x, List))

List = functools.reduce(lambda x,y : x + y, List)

print("Reduced output of Inputed data is :",List)