def pattern(no):
	if no != 0:
		pattern(no-1)
		print(no, end=" ")

def main():
	no = int(input("How many number of numbers you want to print : "))
	pattern(no)
	print()

if __name__ == '__main__':
	main()