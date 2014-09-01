#Fizzbuzz is a silly game that is similar to Cheers Gov'nah.

#Provide a main routine. Use if __name__ == '__main__': to run this function 
#from the command line. For the main routine, you should use sys.argv to get 
# user supplied upper limit.

import sys

def divis(a,b):
	""" is this guy evenly divisible by that guy?"""
	return a%b == 0:


def fizzbuzz(num=100):
	""" output appropriate response re/ divisibility"""
	for value in range(1,num):
		if divis(num,5):
			if divis(num,3):
				print 'fizzbuzz'
			else:
				print 'buzz'
		elif divis(num,3):
			print 'fizz'
		else:
			print num

if __name__ == '__main__':
	num = int(sys.argv[1])
	fizz_buzz(num)



