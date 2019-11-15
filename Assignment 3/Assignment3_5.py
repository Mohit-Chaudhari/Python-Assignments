from MarvellousNum import ChkPrime

No = int(input("How many elements you want to insert into list : "))

List = list()

print("Enter elements : ")
for i in range(No):
	List.append(int(input()))

def ListPrime(List):
	Addition = 0
	for i in List:
		if ChkPrime(i):
			print(i)
			Addition += i
	return Addition

print("Summation of prime numbers from list is",ListPrime(List))