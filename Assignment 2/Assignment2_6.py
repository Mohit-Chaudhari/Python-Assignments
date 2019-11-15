
def Star(n): 
	
	for i in range(0, n): 
	
		for j in range(0, n-i): 
		 
			print("* ",end="") 

		print("\r") 
 
n = int(input("Enter No : "))
Star(n) 
