import threading;


def Upper(str):
	for i in str:
		if i.isupper():
			print("Upper : ",i);


def Lower(str):
	for i in str:
		if i.islower():
			print("Lower : ",i);


def Integer(str):
	for i in str:
		if i.isdigit():
			print("Digit : ",i)

def main():
	string = "Hello World 1234";

	small = threading.Thread(target = Upper, args = (string,));
	capital = threading.Thread(target = Lower, args = (string,));
	digit = threading.Thread(target = Integer, args = (string,));

	small.start();
	capital.start();
	digit.start();


if __name__ == '__main__':
	main();