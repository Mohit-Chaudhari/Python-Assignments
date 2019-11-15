import functools

No = int(input("How many elements : "))

List = list()

print("Enter elements : ", end="")
for i in range(No):
	List.append(int(input()))

def ChkPrime(n) : 
   
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
   
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

List = list(filter(ChkPrime, List))

List = list(map(lambda x : x*2, List))

List = functools.reduce(lambda x,y : max(x,y), List)

print("Mapped and filtered maximum number is",List)