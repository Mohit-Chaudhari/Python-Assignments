def main():
	file1 = "Demo.txt";#input("Enter first file name : ");
	file2 = "ABC.txt";#input("Enter second file name : ");

	f1 = open(file1,'r');
	f2 = open(file2,'r');

	flag = False;

	for d1,d2 in zip(f1,f2):
		if d1 == d2:
			flag = True;
		else:
			flag = False;
			break;

	if flag == True:
		print("Success");
	else:
		print("Failure");

if __name__ == '__main__':
	main();