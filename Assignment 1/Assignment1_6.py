no = int(input("Enter a number : "))


def NumberCheck(no):
	if no == 0:
		print("Zero")
	elif no > 0:
		print("Positive Number")
	else:
		print("Negative Number")

NumberCheck(no)