mark = [(3,4,2.5),(5,6,3.0),(7,9,3.5),(10,12,4.0),(13,15,4.5),(16,19,5.0),(20,22,5.5),(23,26,6.0),(27,29,6.5),(30,32,7.0),(33,34,7.5),(35,36,8.0),(37,38,8.5),(39,40,9.0)]
def change(i):
    for low,high,value in mark:
        if low <= int(i) <= high:
            return value
def round_avg(avg):
    if avg%1 < 0.25: return int(avg) + 0.0
    if 0.75 > avg%1 >= 0.25: return int(avg) + 0.5
    return int(avg) + 1.0
for t in range(int(input())):
    arr = list(input().split())
    sum = 0
    sum += change(arr[0]) + change(arr[1])
    sum += float(arr[2]) + float(arr[3])
    print(round_avg(sum/4))

# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0