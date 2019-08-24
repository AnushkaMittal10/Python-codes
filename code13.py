a=input("Enter your number=")
b=input("Enter power=")
result=1
for i in range(1,b+1):
	if(type(a)==int):
		result=result*a
	elif(type(a)==float):
		result*=a
	else:
		print("Invalid input")
print(result)

