n=int(input("Enter your number="))
fir=0
sec=1
print(fir)
print(sec)
for i in range(1,n+1):
	thi=fir+sec
	fir=sec
	sec=thi
	print(thi)
