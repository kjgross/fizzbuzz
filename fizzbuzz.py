# Count from 1 to N
# If %3 say fizz
# If %5 say buzz
# If both say fizzbuzz
# If neither, print the number
# V1 hardcode N = 100
# V2 let user pick N either when running the script or via raw input
	
		
import sys

if len(sys.argv) == 2:
	max = int(sys.argv[1])
else: 
	max = int(raw_input("Please enter an integer: "))
	
count = 1
for i in range(max+1):
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