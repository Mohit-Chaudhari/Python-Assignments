total = 0

def summation(no):
	global total
	if no != 0:
		rem = no % 10
		no = no // 10
		summation(no)
		total = total + rem

def main():
	no = int(input("Enter number : "))
	summation(no)
	print("Total of inputed number is",total)

if __name__ == '__main__':
	main()