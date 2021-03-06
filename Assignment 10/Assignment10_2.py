import sys;
import os;

def ExtensionChanger(path):

	flag = os.path.isabs(path);
	if flag == False:
		path = os.path.abspath(path)

	exist = os.path.isdir(path)

	if exist:
		cnt = 0;
		for foldername, subfolder, filename in os.walk(path):
			for f in filename:
				if f.endswith(sys.argv[2]):
					base, ext = f.split(".");
					os.rename(foldername+"/"+f,foldername+"/"+base+sys.argv[3]);
					print("Success.")
	else:
		print("Invalid path.")


def main():
	print("--- Mohit Chaudhari ---\n");
	print("Application Name : ", sys.argv[0], "\n");

	if len(sys.argv)!=4:

		if sys.argv[1].lower() == '-h':
			print("Enter dictionary name and file extension. So that we can give you all files with that extension as an output.");
			print("Syntax      : python3 Assignment10_2.py <Folder Name> <Extension of a file>");
			print("For Example : python3 Assignment10_2.py .txt .doc");
		else:
			print("Error : invalid number of arguments.");
			print("Please use -h for help");
			exit();

	try:
		
		ExtensionChanger(sys.argv[1]);

	except Exception:

		print("Something is going wrong...");
		print(Exception);

	finally:

		print("\nThank you for using my application.");


if __name__ == '__main__':
	main()