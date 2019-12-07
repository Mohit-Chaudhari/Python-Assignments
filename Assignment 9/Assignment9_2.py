def main():
	path = input("Enter path : ");
	f = open(path,'r');
	print(f.read());
	f.close();


if __name__ == '__main__':
	main();