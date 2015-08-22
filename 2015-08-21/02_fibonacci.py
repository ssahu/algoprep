# space complexity is O(n)
# store the fibonacci numbers for quick lookup
# time complexity is O(n)
import sys
fib = []

def fibonacci(n):
  if n == 0:
  	return 0
  elif n == 1:
    return 1
  else:
    return fib[n-2] + fib[n-1]

if __name__ == '__main__':
  if len(sys.argv) > 1:
    s = sys.argv[1]
    if s.isdigit():
    	n = int(s)
    else:
    	print 'enter a number not a string'
    	exit(0)
    if n < 0:
      print 'please enter a positive number'
      exit(0)
    for i in range(n):
    	fib.append(fibonacci(i))
    print 'fibonacci:', fib
  else:
    print 'input a number'
    print 'run the program as:'
    print 'syntax: python 02_fibonacci.py <number>'
    print 'example: python 02_fibonacci.py 10'
