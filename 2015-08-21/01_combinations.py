# space complexity is O(n)
# time complexity is O(2^n)
import sys

def recursion_combination(s, length):
#   base case of length 0 combination needed
  if length == 0:
  	return ['']
#   base case if string is smaller than length of combination needed
  if len(s) < length:
    return []
  combinations = []
  for char, idx in zip(s, range(len(s))):
#     here is the kicker
#     example: you need all 2-length combinations of 'abcd'
#     take a character 'a' and then get all 1-length combinations of 'bcd'
#     take a character 'b' and then get all 1-length combinations of 'cd'
#     why not 'acd'? because it was already accounted for when you did
#       by taking the character 'a' - this is the way you prevent
#       repeated combinations.
#     so while recursing, recurse on the substring after the current
#     character
    combinations = combinations + [char + t for t in recursion_combination(s[idx+1:], length - 1)]
  return combinations

if __name__ == '__main__':
  if len(sys.argv) > 1:
    s = sys.argv[1]
    combinations = []
    print 'input string:', s
    for i in range(len(s))[1:]:
#       get combinations of particular length
#       example: get all combinations of length 2 of the string
    	combinations = combinations + recursion_combination(s, i)
    print 'combinations:', combinations
    print 'total number of combinations:', len(combinations)
  else:
    print 'input a word'
    print 'run the program as:'
    print 'syntax: python 01_combinations.py <string>'
    print 'example: python python 01_combinations.py xyzabcdefg'

