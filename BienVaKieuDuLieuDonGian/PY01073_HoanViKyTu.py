from itertools import permutations

s = input()
print('\n'.join([''.join(x) for x in list(permutations(s))]))