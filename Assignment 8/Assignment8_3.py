import threading;


def Even(no):
	sum = 0;
	for i in no:
		if i % 2 == 0:
			sum = sum + i;
	print("Even sum is",sum);


def Odd(no):
	sum = 0;
	for i in no:
		if i % 2 != 0:
			sum = sum + i;
	print("Odd sum is",sum);


def main():
	no = [10,11,12,13,14,15,16];

	evenlist = threading.Thread(target = Even, args = (no,));
	oddlist = threading.Thread(target = Odd, args = (no,));

	evenlist.start();
	oddlist.start();


if __name__ == '__main__':
	main()