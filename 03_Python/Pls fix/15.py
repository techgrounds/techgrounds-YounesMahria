'''
The output should be:
a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
'''
# De patroon = a5|||5|||5||| 3x keer achter elkaar.
# De anedere patroon is 5||| 3x keer achter elkaar na de a.

foo = ''
for i in range(3): # 'a' komt alleen 3 voor en niet 4 dus heb ik 4 naar 3 veranderd. Dit is de patroon waarbij rest onderaan herhaalt weer.
	foo += 'a'
	for j in range(3): # Deze klopt want het komt 3 keer voor per patroon bij de a.
		foo += '5'
		# Voor de 2 codelines hieronder moesten ze gewoon 1 tab naar rechts gaan en verder klopt het met 3 ||| na de 5
		for k in range(3): 
			foo += '|'

print(foo)

