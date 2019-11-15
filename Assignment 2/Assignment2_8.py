
def Star(n): 
	
	for i in range(0, n+1): 
	
		for j in range(0, i): 
		 
			print(j+1," ",end="") 

		print("\r") 
 
n = int(input("Enter No : "))
Star(n) 
