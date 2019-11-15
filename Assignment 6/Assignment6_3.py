class Arithmetic():

	def __init__(self):
		self.Value1 = 0
		self.Value2 = 0

	def Accept(self,n1,n2):
		self.Value1 = n1
		self.Value2 = n2

	def Addition(self):
		return self.Value1+self.Value2

	def Multiplcation(self):
		return self.Value1*self.Value2

	def Division(self):
		return self.Value1/self.Value2

	def Subtraction(self):
		return self.Value1-self.Value2

def main():
	
	Obj1 = Arithmetic()
	Obj1.Accept(20,10)
	print("Additon       : ",Obj1.Addition())
	print("Subtraction   : ",Obj1.Subtraction())
	print("Multiplcation : ",Obj1.Multiplcation())
	print("Division      : ",Obj1.Division())
	print()
	Obj2 = Arithmetic()
	Obj2.Accept(67,12)
	print("Additon       : ",Obj2.Addition())
	print("Subtraction   : ",Obj2.Subtraction())
	print("Multiplcation : ",Obj2.Multiplcation())
	print("Division      : ",Obj2.Division())
	print()
	Obj3 = Arithmetic()
	Obj3.Accept(678,234)
	print("Additon       : ",Obj3.Addition())
	print("Subtraction   : ",Obj3.Subtraction())
	print("Multiplcation : ",Obj3.Multiplcation())
	print("Division      : ",Obj3.Division())

if __name__ == '__main__':
	main()