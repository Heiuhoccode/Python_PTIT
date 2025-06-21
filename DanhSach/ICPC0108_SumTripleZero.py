

for i in range(int(input())):
    n = int(input())
    cnt = 0
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    for ind in range(n):
        left = ind+1
        right = n-1
        while left<right:
            cur_sum = arr[ind] + arr[left] + arr[right]
            if cur_sum == 0:
                cnt += 1
                left += 1
            elif cur_sum < 0:
                left += 1
            else:
                right -= 1
    print(cnt)
# 2
# 5
# 0 -1 2 -3 1
# 5
# 1 -2  1  0  5