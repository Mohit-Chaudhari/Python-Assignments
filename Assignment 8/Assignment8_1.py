import threading

def Even():
	i = 1
	cnt = 0
	while cnt < 10:
		if i % 2 == 0:
			print("Even : ",i);
			cnt += 1
		i += 1

def Odd():
	i = 1
	cnt = 0
	while cnt < 10:
		if not(i % 2 == 0):
			print("Odd  : ",i);
			cnt += 1
		i += 1

if __name__ == '__main__':

	even = threading.Thread(target = Even, args = ());
	odd = threading.Thread(target = Odd, args = ());

	even.start()
	odd.start()