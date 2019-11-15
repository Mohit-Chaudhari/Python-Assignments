def pattern(no):
	if no != 0:
		print(no, end=" ")
		pattern(no-1)

def main():
	no = int(input("How many numbers you want to print : "))
	pattern(no)
	print()

if __name__ == '__main__':
	main()