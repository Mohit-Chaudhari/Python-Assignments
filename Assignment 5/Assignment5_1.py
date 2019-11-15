def pattern(no):
	if no != 0:
		print("*", end=" ")
		pattern(no-1)

def main():
	no = int(input("Enter number of stars you want to print : "))
	pattern(no)
	print()

if __name__ == '__main__':
	main()