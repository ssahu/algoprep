# space complexity is O(n)
# time complexity is O(n)
import sys

def factorial(n):
  if n == 0:
  	return 1
  else:
    return n * factorial(n-1);

if __name__ == '__main__':
  if len(sys.argv) > 1:
    s = sys.argv[1]
    if s.isdigit():
    	n = int(s)
    else:
    	print 'enter a number not a string'
    	exit(0)
    if n < 0:
      print 'factorial of negative numbers:', infinity
      exit(0)
    fact = factorial(n)
    print 'factorial:', fact 
  else:
    print 'input a number'
    print 'run the program as:'
    print 'syntax: python 02_factorial.py <number>'
    print 'example: python 02_factorial.py 10'
