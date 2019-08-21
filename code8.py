max=int(input("Enter your number="))
even_total=0
odd_total=0
for n in range(1,max+1):
	if(n%2==0):
		even_total=even_total+n
	
	else:
		odd_total=odd_total+n
print("Sum of even numbers is=",even_total)
print("Sum of odd numbers is=",odd_total)






