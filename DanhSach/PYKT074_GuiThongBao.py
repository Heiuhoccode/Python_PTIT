for _ in range(int(input())):
    s = input().split()
    res = s[0]
    for i in s[1:]:
        if (len(res) + len(i) + 1 > 100): break
        res += ' ' + i
    print(res)

# Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021