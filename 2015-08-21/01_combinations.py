# space complexity is O(n)
# time complexity is O(2^n)
import sys

def recursion_combination(s, length):
  if length == 0:
  	return ['']
  if len(s) < length:
    return []
  combinations = []
  for char, idx in zip(s, range(len(s))):
    combinations = combinations + [char + t for t in recursion_combination(s[idx+1:], length - 1)]
  return combinations

if __name__ == '__main__':
  if len(sys.argv) > 1:
    s = sys.argv[1]
    combinations = []
    print 'input string:', s
    for i in range(len(s))[1:]:
    	combinations = combinations + recursion_combination(s, i)
    print 'combinations:', combinations
    print 'total number of combinations:', len(combinations)
  else:
    print 'input a word'
    print 'run the program as:'
    print 'syntax: python 01_combinations.py <string>'
    print 'example: python python 01_combinations.py xyzabcdefg'

