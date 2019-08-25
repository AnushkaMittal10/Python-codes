n=int(input("Enter your number="))
print("The divisors of the integer are:")
for i in range(1,n+1):
	if(n%i==0):
		print(i)
