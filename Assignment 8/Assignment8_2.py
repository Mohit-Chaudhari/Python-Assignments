import threading;


def EFactor(no):
	Sum = []
	for i in range(1,no+1):
		if no % i == 0 and i % 2 == 0:
			Sum.append(i);
	print("Even Factor : ",sum(Sum));


def OFactor(no):
	Sum = []
	for i in range(1,no+1):
		if no % i == 0 and i % 2 != 0:
			Sum.append(i);
	print("Odd Factor : ",sum(Sum));


def main():
	no = int(input("Enter number : "));
	OddFactor = threading.Thread(target = EFactor, args = (no,));
	EvenFactor = threading.Thread(target = OFactor, args = (no,));

	OddFactor.start();
	EvenFactor.start();

	OddFactor.join();
	EvenFactor.join();

	print("Exit from main thread.")


if __name__ == '__main__':
	main()