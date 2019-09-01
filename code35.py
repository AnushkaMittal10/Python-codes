a=[]
inp=int(input("Enter number of values you want to insert in array="))
for i in range(0,inp):
	ele=int(input())
	a.append(ele)
print("First array=",a)
b=[]
inp1=int(input("Enter number of valuesyou want to insert for second array="))
for i in range(0,inp1):
	ele=int(input())
	b.append(ele)
print("Second array=",b)

c=[]
if(len(a)==len(b)):
	for i in range(0,len(a)):
		c.append(a[i]+b[i])
	print("\n Sum is=",c)
else:
	print("Please enter same number of values for arrays")

 
