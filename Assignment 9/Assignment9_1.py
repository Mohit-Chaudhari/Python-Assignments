import os;


def main():
	path = input("Enter path : ");
	if os.path.exists(path):
		print("File exists");
	else:
		print("File not exists");


if __name__ == '__main__':
	main();