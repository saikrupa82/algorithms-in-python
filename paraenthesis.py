s=input("Enter any string")
k,j=0,0
for i in s:
	if not i.isalpha():
		if i=="(":
			j+=1
		elif i==")":
			k+=1
if j==k:
	print("The paraenthesis is correct\nVery cool ")
else: 
	print("The paraenthesis is incorrect?\n shame on your part")
	f=input("If u want to know which part enter yes ")
	if f=="yes":
		print("beeeeepppppp")
