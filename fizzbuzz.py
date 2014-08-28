# Count from 1 to N
# If %3 say fizz
# If %5 say buzz
# If both say fizzbuzz
# If neither, print the number
# V1 hardcode N = 100
# V2 let user pick N

## Version 1
count = 1
for i in range(101):
	if i%3 == 0:
		if i%5 == 0:
			print 'fizzbuzz'
			i += 1
		else:
			print 'fizz'
			i += 1
	elif i%5 == 0:
		print 'buzz'
		i += 1
	else:
		print i
		i += 1
		
		
