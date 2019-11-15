class Demo:

	value = None

	def __init__(self,no1,no2):
		self.no1 = no1
		self.no2 = no2

	def fun(self):
		print("No1 : ",self.no1)

	def gun(self):
		print("No2 : ",self.no2)

def main():
	Obj1 = Demo(11,21)
	Obj2 = Demo(51,101)
	Obj1.fun()
	Obj1.gun()
	Obj2.fun()
	Obj2.gun()

if __name__ == '__main__':
	main()