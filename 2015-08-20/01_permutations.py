# space complexity is O(n)
# time complexity is n! - n being the length of string
import sys

def recursion_permutation(s):
  permutations = []
  if len(s) > 2:
#    	if string length is more than 2
# 		then pick each character and recurse
# 		on the remaining characters
    for k, idx in zip(s, range(len(s))):
#     	after picking one character recurse on remaining string
#       example: if you have string 'abc'
#       when you pick 'a', recurse on 'bc'
#       when you pick 'b', recurse on 'ac'
      permutations_each_char = recursion_permutation(s[:idx] + s[idx+1:])
      permutations = permutations + [k + t for t in permutations_each_char]
  elif len(s) == 2:
#     if length of string is 2
#     only 2 permutations possible
#     exacmple: if you have string 'ab'
#     permutations possible 'ab', 'ba'
    permutations = [s, s[::-1]]
  elif len(s) == 1:
#     if string length is 1
#     only that string is the only permutation
    permutations = [s]
  return permutations

if __name__ == '__main__':
  if len(sys.argv) > 1:
    s = sys.argv[1]
    permutations = recursion_permutation(s)
    print 'permutations: ', permutations
    print 'total number of permutations: ', len(permutations)
  else:
    print 'input a word'
    print 'run the program as:'
    print 'syntax: python 01_permutations.py <string>'
    print 'example: python python 01_permutations.py xyzabcdefg'

