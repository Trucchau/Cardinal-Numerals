import pygame
pygame.init()
N = (["không", './vie/north/khong.ogg'], ["một", './vie/north/mot1.ogg'],
     ["hai", './vie/north/hai.ogg'], ["ba", "./vie/north/ba.ogg"],
     ["bốn", './vie/north/bon.ogg'], ["năm", "./vie/north/nam.ogg"],
     ["sáu", "./vie/north/sau.ogg"], ["bảy", "./vie/north/bay.ogg"],
     ["tám", "./vie/north/tam.ogg"], ["chín", "./vie/north/chin.ogg"],
     ["mười", "./vie/north/muoi1.ogg"], ["lăm", "./vie/north/lam.ogg"],
     ["lẻ", './vie/north/le.ogg'], ["mốt", './vie/north/mot2.ogg'],
     ["linh", './vie/north/linh.ogg'], ["mươi", './vie/north/muoi2.ogg'],
     ["nghìn", './vie/north/nghin.ogg'], ["ngàn", './vie/north/ngan.ogg'],
     ["trăm", './vie/north/tram.ogg'], ["triệu", './vie/north/trieu.ogg'],
     ["tỉ", './vie/north/ty.ogg'])

#Nhập số n:
n = int(input("Enter n :"))
#Nhập region:
region = input("Enter region: ")

#Đếm số chữ số của n:
def count_number(n):
    i = 10
    s = 1
    while i <= 1000000000000:
        a = n // i
        if a == 0:
            sochuso = s
            break
        s += 1
        i *= 10
    return sochuso

#Đọc số có 2 chữ số:
def read_2(N, n):
    ans = []
    sodautien = n // 10
    sothu2 = n % 10
    if sodautien == 1:
        if sothu2 == 5:
            ans = "mười lăm"
        elif sothu2 != 0:
            ans = "mười " + N[sothu2][0]
        else:
            ans = "mười"
    else:
        if sothu2 == 5:
            ans = N[sodautien][0] + " mươi lăm"
        elif sothu2 == 1:
            ans = N[sodautien][0] + " mươi mốt"
        elif sothu2 != 0:
            ans = N[sodautien][0] + " mươi " + N[sothu2][0]
        else:
            ans = N[sodautien][0] + " mươi"
    return ans

#Đọc số có 3 chữ số (trường hợp số bé hơn 1000)
def read_3_1(N, n):
    ans = []
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sohangchuc == 0:
        ans = N[sodautien][0] + " trăm"
    elif sothu2 == 0:
        ans = N[sodautien][0] + " trăm linh " + N[sothu3][0]
    else:
        ans = N[sodautien][0] + " trăm " + read_2(N, sohangchuc)
    return ans

#Đọc số có 3 chữ số (trường hợp số ở vị trí hàng trăm trong số n > 1000)
def read_3_2(N, n):
    ans = []
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sodautien == 0 and sothu2 != 0:
        ans = "không trăm " + read_2(N, sohangchuc)
    elif sodautien == 0 and sothu2 == 0 and sothu3 != 0:
        ans = "không trăm linh " + N[sothu3][0]
    elif sodautien != 0:
        ans = read_3_1(N, n)
    elif sodautien == 0 and sothu2 == 0 and sothu3 == 0:
        ans = ""
    return ans

#Đọc số hàng ngàn:
def read_thousand(N, n):
    ans = []
    sohangngan = n // 1000
    sohangtram = n % 1000
    if count_number(sohangngan) == 2:
        ans = read_2(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif count_number(sohangngan) == 3:
        ans = read_3_1(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan < 10 and sohangngan > 0:
        ans = N[sohangngan][0] + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan == 0:
        ans = read_3_2(N, sohangtram)
    return ans

def read_thousand_2(N, n):
    ans = []
    sohangngan = n // 1000
    sohangtram = n % 1000
    if sohangngan < 100:
        ans = read_3_2(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan < 10:
        ans = read_3_2(N, sohangngan) + "nghìn" + read_3_2(N, sohangtram)
    elif sohangngan == 0:
        ans = read_3_2(N, sohangtram)
    return ans

#Đọc số hàng triệu:
def read_million(N, n):
    ans = []
    sohangtrieu = n // 1000000
    sohangngan = n % 1000000
    if count_number(sohangtrieu) == 2:
        ans = read_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif count_number(sohangtrieu) == 3:
        ans = read_3_1(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangtrieu < 10 and sohangtrieu > 0:
        ans = N[sohangtrieu][0] + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangtrieu == 0:
        ans = read_thousand(N, sohangngan)
    return ans

def read_million_2(N, n):
    ans = []
    sohangtrieu = n // 1000000
    sohangngan = n % 1000000
    if sohangtrieu < 100:
        ans = read_3_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangngan < 10:
        ans = read_3_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangngan == 0:
        ans = read_thousand(N, sohangngan)
    return ans


#Đọc số hàng tỉ:
def read_billion(N, n):
    ans = []
    sohangty = n // 1000000000
    sohangtrieu = n % 1000000000
    if count_number(sohangty) == 2:
        ans = read_2(N, sohangty) + " tỉ " + read_million_2(N, sohangtrieu)
    elif count_number(sohangty) == 3:
        ans = read_3_1(N, sohangty) + " tỉ " + read_million_2(N, sohangtrieu)
    elif sohangty < 10 and sohangty > 0:
        ans = N[sohangty][0] + " tỉ " + read_million_2(N, sohangtrieu)
    elif sohangty == 0:
        ans = read_million(N, sohangtrieu)
    return ans

#Hàm tổng:
def integer_to_vietnamese_numeral(n, region):
    if not isinstance(n, int):
        raise TypeError("Not an integer.")
    if n < 0:
        raise ValueError("Not positive integer.")
    if n > 999999999999:
        raise OverflowError
    if n <= 10:
        result = N[n][0]
    elif n > 10 and n <= 100:
        result = read_2(N,n)
    else:
        if not isinstance(region, str):
            raise TypeError      
        if region == 'south':
            result1 = read_billion(N, n).replace("nghìn", "ngàn")
            result = result1.replace("linh", "lẻ")
        elif region == 'north' or region == '' or region == '':
            result = read_billion(N, n)
        else:
            raise ValueError

    for i in result.split():
        for j in N:
            if i == j[0]:

                sound = pygame.mixer.Sound(j[1])
                sound.play()
                pygame.time.wait(600)

    return result

print(integer_to_vietnamese_numeral(n, region))