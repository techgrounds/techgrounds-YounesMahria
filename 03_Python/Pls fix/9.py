'''
The output should be:
0
1
2
3
4
8
9
'''
for i in range(10):
	if i < 5:
		print(i)
	elif i > 7: # First we need to change the elif i < 8: to elif i > 7 
		print(i)
		# break # Remove the break since we still need to keep going and not stop if i is at 5
	# else:
		# print(i)
  
  