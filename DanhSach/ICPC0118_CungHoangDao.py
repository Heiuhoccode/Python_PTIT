def ten(d,m):
    if (m==3 and d>=21) or (m==4 and d<=19):
        return "Bach Duong"
    elif (m==4 and d>=20) or (m==5 and d<=20):
        return "Kim Nguu"
    elif (m==5 and d>=21) or (m==6 and d<=20):
        return "Song Tu"
    elif (m==6 and d>=21) or (m==7 and d<=22):
        return "Cu Giai"
    elif (m==7 and d>=23) or (m==8 and d<=22):
        return "Su Tu"
    elif (m==8 and d>=23) or (m==9 and d<=22):
        return "Xu Nu"
    elif (m==9 and d>=23) or (m==10 and d<=22):
        return "Thien Binh"
    elif (m==10 and d>=23) or (m==11 and d<=22):
        return "Thien Yet"
    elif (m==11 and d>=23) or (m==12 and d<=21):
        return "Nhan Ma"
    elif (m==12 and d>=22) or (m==1 and d<=19):
        return "Ma Ket"
    elif (m==1 and d>=20) or (m==2 and d<=18):
        return "Bao Binh"
    return "Song Ngu"
# ListCHD.append(CHD("Bach Duong","21/03", "19/04"))
# ListCHD.append(CHD("Kim Nguu","20/04", "20/05"))
# ListCHD.append(CHD("Song Tu","21/05", "20/06"))
# ListCHD.append(CHD("Cu Giai","21/06", "22/07"))
# ListCHD.append(CHD("Su Tu","23/07", "22/08"))
# ListCHD.append(CHD("Xu Nu","23/08", "22/09"))
# ListCHD.append(CHD("Thien Binh","23/09", "22/10"))
# ListCHD.append(CHD("Thien Yet","23/10", "22/11"))
# ListCHD.append(CHD("Nhan Ma","23/11", "21/12"))
# ListCHD.append(CHD("Ma Ket","22/12", "31/12"))
# ListCHD.append(CHD("Ma Ket","01/01", "19/01"))
# ListCHD.append(CHD("Bao Binh","20/01", "18/02"))
# ListCHD.append(CHD("Song Ngu","19/02", "20/03"))

# for i in ListCHD:
#     print(i.getDau())
for _ in range(int(input())):
    d,m = map(int,input().split())
    print(ten(d,m))