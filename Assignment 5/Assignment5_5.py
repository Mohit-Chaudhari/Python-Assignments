Factorial = 1

def fact(no):
	global Factorial;
	if no >= 1:
		fact(no-1)
		Factorial *= no

def main():
	no = int(input("Enter number : "))
	fact(no)
	print("Factorial of",no,"is",Factorial)

if __name__ == '__main__':
	main()