for i in range(int(input())):
    s1 = input()
    s2 = input()
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        print(f'Test {i+1}: YES')
    else:
        print(f'Test {i+1}: NO')

# 4
# testing
# intestg
# abc
# aabbbcccc
# abcabcbcc
# aabbbcccc
# abc
# xyz