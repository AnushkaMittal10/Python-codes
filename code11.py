len=int(input("Enter length for the reactangle="))
brth=int(input("Enter breadth for the rectangle="))
choice=input("Enter the operation you want to perform=")
if(choice=="area"):
	area=len*brth
	print("Area of rectangle is=",area)
elif(choice=="perimeter"):
	perimeter=2*(len+brth)
	print("Perimeter of rectangle is=",perimeter)
elif(choice=="diogonal"):
	diogonal=sqrt((l*l)+(b*b))
	print("Diogonals of rectangle is=",diogonal)
else:
	print("You entered invalid choice")


