s=int(input("Enter any number"))
ls=[]
k,max,min=0,0,0
f=str(s)
if f.isdigit:
	for i in range(1,s+1):

		k+=i

		ls.append(i)
print(ls)
print("Average of number is",k/s)
max=ls[0]
for i in ls:
	if max<i:
		max=i
print("Maximum number is ",max)
min=ls[0]
for i in ls:
	if min>i:
		min=i
print("Maximum number is ",min)


