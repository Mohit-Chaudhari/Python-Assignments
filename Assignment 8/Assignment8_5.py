import threading;


def forward(no):
	if no != 0:
		forward(no-1);
		print(no);

def reverse(no):
	if no != 0:
		print(no);
		reverse(no-1);

def main():
	thread1 = threading.Thread(target = forward, args = (50,));
	thread2 = threading.Thread(target = reverse, args = (50,));

	thread1.start();
	thread1.join();
	print("*"*50);
	thread2.start();


if __name__ == '__main__':
	main();