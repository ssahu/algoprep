# space complexity is O(n)
# time complexity is n! - n being the length of string
import sys

def recursion_permutation(str):
  permutations = []
  if len(str) > 2:
#    	if string length is more than 2
# 		then pick each character and recurse
# 		on the remaining characters
    for k, idx in zip(str, range(len(str))):
#     	after picking one character recurse on remaining string
#       example: if you have string 'abc'
#       when you pick 'a', recurse on 'bc'
#       when you pick 'b', recurse on 'ac'
      permutations_each_char = recursion_permutation(str[:idx] + str[idx+1:])
      permutations = permutations + [k + t for t in permutations_each_char]
  elif len(str) == 2:
#     if length of string is 2
#     only 2 permutations possible
#     exacmple: if you have string 'ab'
#     permutations possible 'ab', 'ba'
    permutations = [str, str[::-1]]
  elif len(str) == 1:
#     if string length is 1
#     only that string is the only permutation
    permutations = [str]
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

