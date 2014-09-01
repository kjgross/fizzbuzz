#Fizzbuzz is a silly game that is similar to Cheers Gov'nah.

#Provide a main routine. Use if __name__ == '__main__': to run this function 
#from the command line. For the main routine, you should use sys.argv to get 
# user supplied upper limit.

import sys

def divis(a,b):
	if a%b == 0:
		return True
	else:
		return False

def fizzbuzz(num=100):
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
	if len(sys.argv) == 2:
		while True:
			try:
				sys.argv[1] = int(sys.argv[1])
				maxfizz = int(sys.argv[1])
				break
			except ValueError:
				maxfizz = int(raw_input("Not a valid integer! Please try again. "))
				break
	else: 
		maxfizz = int(raw_input("Please enter an integer: "))
	count = 1
	while count < maxfizz + 1:
		fizzbuzz(count)
		count += 1



