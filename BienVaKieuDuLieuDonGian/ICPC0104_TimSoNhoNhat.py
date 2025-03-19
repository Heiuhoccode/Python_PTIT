import re
for t in range(int(input())):
    print(min(int(i) for i in re.findall(r'\d+', input())))
# 2
# 2ab29cd19
# ab123gh456cd
