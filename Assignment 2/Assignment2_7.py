
def Star(n): 
	
	for i in range(0, n): 
	
		for j in range(0, n): 
		 
			print(j+1," ",end="") 

		print("\r") 
 
n = int(input("Enter No : "))
Star(n)