import re
for t in range(int(input())):
    print(max(int(i) for i in re.findall(r'\d+', input())))
# 2
# 2ab29cd19
# ab123gh456cd
