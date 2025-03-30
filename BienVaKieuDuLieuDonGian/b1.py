def day_con_tong_nho_nhat(lst):
    if not lst:
        return []

    min_sum = float('inf')
    current_sum = 0
    start = 0
    min_start = 0
    min_end = 0

    for i, num in enumerate(lst):
        if current_sum > 0:
            current_sum = num
            start = i
        else:
            current_sum += num

        if current_sum < min_sum:
            min_sum = current_sum
            min_start = start
            min_end = i

    return lst[min_start:min_end+1]
print((day_con_tong_nho_nhat(list(map(int,input().split())))))