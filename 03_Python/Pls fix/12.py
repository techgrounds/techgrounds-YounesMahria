'''
The output should be:
4
16129
'''
def square(x):
	return x**2

nr = square(2)
print(nr)

foo = 127

big = square(foo)
print(big)

# foo = 127 # variable is defined too late, remember it reads from top to bottom.