import sys;

def main():
	path = sys.argv[1]
	with open(path,"r") as f:
		with open("Demo.txt","w") as f1:
			for line in f:
				f1.write(line);

if __name__ == '__main__':
	main();