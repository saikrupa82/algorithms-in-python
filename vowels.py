s=input("Enter any word")

def vowco(s):
	r,f,g,k=0,0,0,0
	for i in s:
	
		if i.isalpha():
			if i=="a"or i=="o" or i=="i"or i=="u"or i=="e" :
				r+=1
			else:
				g+=1
		elif not i.isalnum():
			f+=1
		elif i.isnumeric():
			k+=1
	return("This vowels are",r,"\nThe special character are",f,"\nThe constonts are",g,"\nThe digits are ",k)
	

print(vowco(s))
