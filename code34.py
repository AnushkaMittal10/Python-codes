d=[]
a=int(input("Enter the numbers for array="))
while True:
	if len(d) == a:
		break

	ele=int(input())
	if ele in d:
		print("Number already in array")
		continue

	d.append(ele)

print("Array is:",d)
search=int(input("Enter the number you want to search in array="))
if search in d:
	print("Number searched:",search)
else:	
	print("Number not found")


