lst=[]

nelst=[]

a=eval(input("Enter any number"))

def div(a):

	for i in range(1,51):

		lst.append(i)

	for i in lst:

		if i%a==0:

			nelst.append(i)

		nelst.remove(a)

	return(nelst)

print(div(a))
	
	
