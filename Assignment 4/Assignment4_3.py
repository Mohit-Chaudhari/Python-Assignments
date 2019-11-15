import functools

No = int(input("How many elements : "))

List = []

print("Enter elements : ")
for i in range(No):
	List.append(int(input()))

List = list(filter(lambda x : x >= 70 and x <= 90, List))

List = list(map(lambda x : x+10, List))

X = functools.reduce(lambda x,y : x*y, List)

print("Reduced output of given input is",X)