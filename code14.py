n=int(input("Enter your number="))
if n<=2:
	print("It's a prime number")
else:
	flag=True
	for i in range(2,int(n/2)+1):
		if n%i==0:
			print("Not a prime number")
			flag=False
			break
	if  flag:
		print("It's a prime number")
