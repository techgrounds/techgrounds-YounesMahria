'''
The output should be:
True
'''
def rtn(x):
	return(x)

foo = rtn(3) # You literally input number 3 only to get 3 back from the function rtn as in return. I could change the 3 into 5 or higher

if foo < rtn(4): # To make it true it is suppose to be lower than and not higher than. 3 is lower than 4 to get true.
	print(True)
else:
	print(False)