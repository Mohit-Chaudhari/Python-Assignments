import shutil;
import os;
import sys;

def FileCopier(src,dest):

	flag = os.path.isabs(src);
	if flag == False:
		src = os.path.abspath(src)

	src_exist = os.path.isdir(src);
	
	flag = os.path.isabs(dest);
	if flag == False:
		dest = os.path.abspath(dest);

	if os.path.isdir(dest) == False:
		os.mkdir(dest);
		dest_exist = os.path.isdir(dest);
	else:
		dest_exist = False;
		print(dest+" already exist.");

	if src_exist and dest_exist:
		for foldername, subfolder, filename in os.walk(src):
			for f in filename:
				shutil.copy(foldername+"/"+f, dest);


def main():
	print("--- Mohit Chaudhari ---\n");
	print("Application Name : ", sys.argv[0], "\n");

	if len(sys.argv)!=3 :

		if sys.argv[1].lower() == '-h':
			print("Enter src directory and Destination directory. It will copy src files to destination.");
			print("Syntax      : python3 Assignment10_3.py <SRC Folder Name> <DEST Folder Name>");
			print("For Example : python3 Assignment10_3.py Demo Demo1");
		else:
			print("Error : invalid number of arguments.");
			print("Please use -h for help");
			exit();

	try:
		
		if len(sys.argv) == 3:	
			FileCopier(sys.argv[1],sys.argv[2]);

	except Exception:

		print("Something is going wrong...");
		print(Exception);

	finally:

		print("\nThank you for using my application.");


if __name__ == '__main__':
	main()