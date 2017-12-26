def sort(s):
	s=sorted(s.split(","))
	s=",".join(s)
	return s
s=input("Enter a comma separated string of words ")
print(sort(s))
