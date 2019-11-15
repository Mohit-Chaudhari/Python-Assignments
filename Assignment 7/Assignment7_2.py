class BankAccount:

	ROI = 10.5

	def __init__(self, Name, Amount):
		self.Name = Name
		self.Amount = Amount

	def Display(self):
		print("Name   : ",self.Name)
		print("Amount : ",self.Amount)
		print()

	def Deposite(self, Amount):
		self.Amount += Amount

	def Withdraw(self, Amount):
		self.Amount -= Amount

	def CalculateInterest(self):
		self.Amount *= BankAccount.ROI

def main():
	OBJ1 = BankAccount("Mohit", 1000)
	OBJ1.Display()
	OBJ1.Deposite(1400)
	OBJ1.Display()
	OBJ1.Withdraw(800)
	OBJ1.Display()
	OBJ1.CalculateInterest()
	OBJ1.Display()

if __name__ == '__main__':
	main()