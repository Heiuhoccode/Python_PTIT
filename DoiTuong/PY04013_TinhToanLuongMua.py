from datetime import *

class Station_rain:
    def __init__(self, id, name,  begin, end, rain):
        self.id = "T0" + str(id)
        self.name = name
        self.begin = datetime.strptime(begin, "%H:%M")
        self.end = datetime.strptime(end, "%H:%M")
        self.rain = rain

    def times(self):
        return (self.end - self.begin).total_seconds() / 3600

    def __str__(self):
        return f'{self.id} {self.name}'
stations = []
name_id = {}
setName = []
cnt = 1
for t in range(int(input())):
    name = input()
    begin = input()
    end = input()
    rain = float(input())
    if name not in name_id:
        name_id[name] = cnt
        cnt+=1
    if name not in setName:
        setName.append(name)
    station = Station_rain(name_id[name], name, begin, end,rain)
    stations.append(station)

setStation = set()
# print(setName)
for i in setName:
    sumRain = 0
    sumTimes = 0
    for j in stations:
        if j.name == i:
            sumRain += j.rain
            sumTimes += j.times()
    for j in stations:
        if j.name == i:
            print(f'{j} {(sumRain/sumTimes):.2f}')
            break
# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35