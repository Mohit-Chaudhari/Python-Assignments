class Circle():

	PI = 3.14
	
	def __init__(self):
		self.Radius = 0.0
		self.Area = 0.0
		self.Circumference = 0.0
		
	def Accept(self, Radius):
		self.Radius = Radius

	def CalculateArea(self):
		self.Area = self.PI*self.Radius*self.Radius

	def CalculateCircumference(self):
		self.Circumference = 2*self.PI*self.Radius
		pass

	def Display(self):
		print("Radius                  : ",self.Radius)
		print("Area of Circle          : ",self.Area)
		print("Circumference of Circle : ",self.Circumference)

def main():
	C1 = Circle()
	C1.Accept(10)
	C1.CalculateArea()
	C1.CalculateCircumference()
	C1.Display()

if __name__ == '__main__':
	main()