import os
import pygame
pygame.init()
N = (["không", './vie/north/khong.ogg', './sou/Khong.ogg'], ["một", './vie/north/mot1.ogg', './sou/Mot.ogg'],
     ["hai", './vie/north/hai.ogg', './sou/Hai.ogg'], ["ba", "./vie/north/ba.ogg", './sou/Ba.ogg'],
     ["bốn", './vie/north/bon.ogg', './sou/Bon.ogg'], ["năm", "./vie/north/nam.ogg", './sou/Nam.ogg'],
     ["sáu", "./vie/north/sau.ogg", './sou/Sau.ogg'], ["bảy", "./vie/north/bay.ogg", './sou/Bay.ogg'],
     ["tám", "./vie/north/tam.ogg", './sou/Tam.ogg'], ["chín", "./vie/north/chin.ogg", './sou/Chin.ogg', ],
     ["mười", "./vie/north/muoi1.ogg", './sou/Muoi1.ogg'], ["lăm", "./vie/north/lam.ogg", './sou/Lam.ogg'],
     ["lẻ", './vie/north/le.ogg', './sou/Le.ogg'], ["mốt", './vie/north/mot2.ogg', './sou/mot1.ogg'],
     ["linh", './vie/north/linh.ogg', './sou/Linh.ogg'], ["mươi", './vie/north/muoi2.ogg', './sou/Muoi.ogg'],
     ["nghìn", './vie/north/nghin.ogg', './sou/Nghin.ogg'], ["ngàn", './vie/north/ngan.ogg', './sou/Ngan.ogg'],
     ["trăm", './vie/north/tram.ogg', './sou/Tram.ogg'], ["triệu", './vie/north/trieu.ogg', './sou/Trieu.ogg'],
     ["tỉ", './vie/north/ty.ogg', './sou/Ti.ogg'])

#Nhập số n:
n = int(input("Enter n :"))
#Nhập region:
region = input("Enter region: ")
a = input("Do you want to activate Text-to-speech? (True or False ?)") #Nhap cau hoi co muon kich hoat che do text to speech?
if a == "True" or a == "true":
    activate_tts = True                 #Chuyen doi cau tra loi sang kieu ky tu Boolean
elif a == "False" or a == "false":
    activate_tts = False
else:
    activate_tts = a                    #Neu cau tra loi khong phai la True /False, du lieu se khong chuyen doi ve kieu Boolean va raise TypeError


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
        ans = " "
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
    if sohangngan == 0:
        ans = read_3_2(N, sohangtram)
    elif sohangngan < 10 and sohangngan >0:
        ans = read_3_2(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan < 100:
        ans = read_3_2(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan >= 100:
        ans = read_thousand(N,n)
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
    if sohangtrieu == 0:
        ans = read_thousand_2(N, sohangngan)
    elif sohangtrieu < 10 and sohangtrieu > 0:
        ans = read_3_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangtrieu < 100:
        ans = read_3_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangtrieu >= 100:
        ans = read_million(N,n)
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
def integer_to_vietnamese_numeral(n, region = 'north', activate_tts = False):


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
            if activate_tts == True:
                for i in result.split():
                    for j in N:
                        if i == j[0]:
                            sound = pygame.mixer.Sound(j[2])
                            sound.play()
                            pygame.time.wait(1100)
                            pygame.mixer.stop()
            elif activate_tts != "" and not isinstance(activate_tts, bool):
                raise TypeError
        elif region == 'north' or region == '' or region == '':
            result = read_billion(N, n)
            if activate_tts == True:
                for i in result.split():
                    for j in N:
                        if i == j[0]:
                            sound = pygame.mixer.Sound(j[1])
                            sound.play()
                            pygame.time.wait(750)
                            pygame.mixer.stop()
            elif activate_tts != "" and not isinstance(activate_tts, bool):
                raise TypeError
        else:
            raise ValueError

    return result

<<<<<<< HEAD:Cardinal_Numerals.py
print(integer_to_vietnamese_numeral(n, region, activate_tts))

=======
print(integer_to_vietnamese_numeral(n, region))
os.system("PAUSE")
>>>>>>> 7c9ea9d296e59692d72a70a565fe592f16a1e5b3:Cardinal Vietnamese Number.py
