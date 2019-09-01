d=[]
a=int(input("Enter the numbers for array="))
for i in range(0,a):
	ele=int(input())
	d.append(ele)
print("Array is:",d)
search=int(input("Enter the number you want to search in array="))
if search in d:
	print("Number searched:",search)
else:
	print("Number not found")


