def xoayvong(s,sample):
    temp = s
    cnt = 0
    while temp != sample:
        if cnt == len(s):
            return -1
        temp = temp[1:] + temp[0]
        cnt += 1

    return cnt
def process(i, arr):
    cnt = 0
    for j in range(len(arr)):
        if j != i:
            if xoayvong(arr[j],arr[i]) == -1:
                return -1
            cnt += xoayvong(arr[j],arr[i])
    return cnt
arr = []
for t in range(int(input())):
    arr.append(input())
arr_xoayvong = []
temp = 0
for i in range(len(arr)):
    if process(i,arr) == -1:
        print("NO")
        temp = 1
        break
    else:
        arr_xoayvong.append(process(i,arr))
if temp != 1:
    print(min(arr_xoayvong))
# 4
# xzzwo
# zwoxz
# zzwox
# xzzwo