class Numbers:

	def __init__(self, value):
		self.value = value

	def ChkPrime(self):
		 
	    if (self.value <= 1) : 
	        return False
	    if (self.value <= 3) : 
	        return True
	    if (self.value % 2 == 0 or self.value % 3 == 0) : 
	        return False
	    i = 5
	    while(i * i <= self.value) : 
	        if (self.value % i == 0 or self.value % (i + 2) == 0) : 
	            return False
	        i = i + 6
	  
	    return True

	def ChkPerfect(self):
		print("SumFactors : ",self.SumFactors())
		if self.SumFactors()-self.value == self.value:
			return True
		else:
			return False

	def SumFactors(self):
		sum1 = 0
		print()
		for i in range(1, self.value + 1):
			if self.value % i == 0:
				sum1 = sum1 + i
		return sum1

	def Factors(self):
		print("The factors of",self.value,"are:")
		for i in range(1, self.value + 1):
			if self.value % i == 0:
				print(i)

def main():
	NO = int(input("Enter number : "))
	OBJ1 = Numbers(NO)
	if OBJ1.ChkPrime() == True:
		print("Prime Number")
	else:
		print("Not Prime")

	OBJ1.Factors()
	if OBJ1.ChkPerfect() == True:
		print("Perfect number")
	else:
		print("Not perfect number")

if __name__ == '__main__':
	main()