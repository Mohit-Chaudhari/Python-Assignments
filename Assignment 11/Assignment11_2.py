import sys;
import os;
import hashlib;


def hashfile(path, blocksize = 1024):
	afile = open(path, 'rb');
	hasher = hashlib.md5();
	buf = afile.read(blocksize);
	while(len(buf) > 0):
		hasher.update(buf);
		buf = afile.read(blocksize);
	afile.close();
	return hasher.hexdigest();

def DuplicateFileDetector(path):
	flag = os.path.isabs(path);
	if flag == False:
		path = os.path.abspath(path)

	exist = os.path.isdir(path);

	Duplicates = {};

	if exist:
		for folder, subfolders, files in os.walk(path):
			for f in files:
				path = os.path.join(folder,f);
				file_hash = hashfile(path)

				if file_hash in Duplicates:
					Duplicates[file_hash].append(path);
				else:
					Duplicates[file_hash] = [path];

	results = list(filter(lambda x:len(x) > 1 ,Duplicates.values()));

	log = open('Log.txt','w+');

	if len(results) > 0:
		print("Duplicates found.");
		print("Duplicate files are stored into Log.txt file of same folder");
		for result in results:
			for subresult in result:
				#print("\t",subresult);
				log.write(subresult);

def main():
	print("--- Mohit Chaudhari ---");

	if len(sys.argv) == 2:
		if sys.argv[1].lower() == '-h':
			print("This script is use to find checksum of file.");
			print("Usage : python3 Assignment11_1.py <Folder Name>");
			print("Example : python3 Assignment11_1.py Demo");
			exit();
		else:

			DuplicateFileDetector(sys.argv[1]);
	else:
		print("Invalid number of arguments.");
		print("Please use '-h' for help.")
		exit();



if __name__ == '__main__':
	main();