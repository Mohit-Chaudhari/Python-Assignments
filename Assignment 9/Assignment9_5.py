path = 'ABC.txt'#input("Enter file name : ");
key = input("Enter keyword to search : ");

f1 = open(path,'r');

count = f1.read().count(key);

print(count);