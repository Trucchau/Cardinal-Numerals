import pygame
pygame.init()
N = (["không", './vie/north/khong.ogg', './vie/sou/Khong.ogg'], ["một", './vie/north/mot1.ogg', './vie/sou/Mot.ogg'],
     ["hai", './vie/north/hai.ogg', './vie/sou/Hai.ogg'], ["ba", "./vie/north/ba.ogg", './vie/sou/Ba.ogg'],
     ["bốn", './vie/north/bon.ogg', './vie/sou/Bon.ogg'], ["năm", "./vie/north/nam.ogg", './vie/sou/Nam.ogg'],
     ["sáu", "./vie/north/sau.ogg", './vie/sou/Sau.ogg'], ["bảy", "./vie/north/bay.ogg", './vie/sou/Bay.ogg'],
     ["tám", "./vie/north/tam.ogg", './vie/sou/Tam.ogg'], ["chín", "./vie/north/chin.ogg", './vie/sou/Chin.ogg', ],
     ["mười", "./vie/north/muoi1.ogg", './vie/sou/Muoi1.ogg'], ["lăm", "./vie/north/lam.ogg", './vie/sou/Lam.ogg'],
     ["lẻ", './vie/north/le.ogg', './vie/sou/Le.ogg'], ["mốt", './vie/north/mot2.ogg', './vie/sou/mot1.ogg'],
     ["linh", './vie/north/linh.ogg', './vie/sou/Linh.ogg'], ["mươi", './vie/north/muoi2.ogg', './vie/sou/Muoi.ogg'],
     ["nghìn", './vie/north/nghin.ogg', './vie/sou/Nghin.ogg'], ["ngàn", './vie/north/ngan.ogg', './vie/sou/Ngan.ogg'],
     ["trăm", './vie/north/tram.ogg', './vie/sou/Tram.ogg'], ["triệu", './vie/north/trieu.ogg', './vie/sou/Trieu.ogg'],
     ["tỉ", './vie/north/ty.ogg', './vie/sou/Ti.ogg'])

A = (["zero", './eng/Zero.ogg'], ["one",'./eng/one.ogg'], ["two",'./eng/two.ogg'],
     ["three",'./eng/three.ogg'], ["four",'./eng/four.ogg'], ["five",'./eng/five.ogg'],
     ["six",'./eng/Six.ogg'], ["seven",'./eng/Seven.ogg'], ["eight", './eng/Eight.ogg'],
     ["nine",'./eng/Nine.ogg'], ["ten",'./eng/Ten.ogg'],['eleven','./eng/Eleven.ogg'],
     ['twelve','./eng/Twelve.ogg'],['thirteen','./eng/Thirteen'],['fourteen','./eng/Fourteen.ogg'],
     ['fifteen','./eng/Fifteen.ogg'],['sixteen','.eng/Sixteen.ogg'],['seventeen','./eng/Seventeen.ogg'],
     ['eighteen','./eng/Eighteen.ogg'],['nineteen','./eng/Nineteen.ogg'],['twenty','./eng/Twenty.ogg'],
     ['thirty','./eng/Thirty.ogg'],['fourty','./eng/Fourty.ogg'],['fifty','./eng/Fifty.ogg'],
     ['sixty','./eng/Sixty.ogg'],['seventy','./eng/Seventy.ogg'],['eighty','./eng/Eighty.ogg'],
     ['ninety','./eng/Ninety.ogg'],['hundred','./eng/Hundred.ogg'],['thousand','./eng/Thousand.ogg'],
     ['million','./eng/Million.ogg'],['billion','./eng/Billion.ogg'],['and','./eng/And.ogg'])




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
    ans = ""
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
    ans = ""
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
    ans = ""
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
    ans = ""
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
    ans = ""
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
    ans = ""
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



# Đọc số có 2 chữ số:
def read_2_en(A, n):
    ans = ""
    sodautien = n // 10
    sothu2 = n % 10

    if sodautien == 1:
        if sothu2 == 0:
            ans = "ten"
        elif sothu2 == 1:
            ans = "eleven"
        elif sothu2 == 2:
            ans = "twelve"
        elif sothu2 == 3:
            ans = "thirteen"
        elif sothu2 == 5:
            ans = "fifteen"
        else:
            ans = A[sothu2][0] + "teen"
    elif sodautien == 2:
        if sothu2 == 0:
            ans = "twenty"
        else:
            ans = "twenty" + "-" + A[sothu2][0]
    elif sodautien == 5:
        if sothu2 == 0:
            ans = "fifty"
        else:
            ans = "fifty" + "-" + A[sothu2][0]
    elif sodautien == 3:
        if sothu2 == 0:
            ans = "thirty"
        else:
            ans = "thirty" + "-" + A[sothu2][0]
    elif sodautien == 0:
        ans = A[sothu2][0]
    else:
        if sothu2 == 0:
            ans = A[sodautien][0] + 'ty'
        else:
            ans = A[sodautien][0] + "ty" + "-" + A[sothu2][0]
    ans = ans.replace("tt", "t")
    return ans


# Đọc số có 3 chữ số:
def read_3_1_en(A, n):
    ans = ""
    sodautien = n // 100
    sohangchuc = n % 100
    if sohangchuc == 0:
        ans = A[sodautien][0] + " hundred"
    else:
        ans = A[sodautien][0] + " hundred and " + read_2_en(A, sohangchuc)
    return ans


# Đọc số có 3 chữ số (trường hợp số ở vị trí hàng trăm trong số n > 1000)
def read_3_2_en(A, n):
    ans = ""
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sodautien == 0 and sothu2 != 0:
        ans = " and " + read_2_en(A, sohangchuc)
    elif sodautien != 0:
        ans = " and " + read_3_1_en(A, n)
    elif sodautien == 0 and sothu2 == 0 and sothu3 == 0:
        ans = ""
    return ans


# Đọc số hàng ngàn:
def read_thousand_en(A, n):
    ans = ""
    sohangngan = n // 1000
    sohangtram = n % 1000
    if count_number(sohangngan) == 2:
        ans = read_2_en(A, sohangngan) + " thousand" + read_3_2_en(A, sohangtram)
    elif count_number(sohangngan) == 3:
        ans = read_3_1_en(A, sohangngan) + " thousand" + read_3_2_en(A, sohangtram)
    elif sohangngan < 10 and sohangngan > 0:
        ans = A[sohangngan][0] + " thousand" + read_3_2_en(A, sohangtram)
    elif sohangngan == 0:
        ans = read_3_1_en(A, sohangtram)
    return ans


def read_thousand_2_en(A, n):
    ans = ""
    sohangngan = n // 1000
    sohangtram = n % 1000
    if sohangngan == 0:
        ans = read_3_2_en(A, sohangtram)
    elif sohangngan < 10 and sohangngan > 0:
        ans = ", " + A[sohangngan][0] + " thousand" + read_3_2_en(A, sohangtram)
    elif sohangngan < 100:
        ans = ', '+ read_3_2_en(A, sohangngan) + "thousand" + read_3_2_en(A, sohangtram)
    else:
        ans = ", " + read_thousand_en(A, n)
    return ans


# Đọc số hàng triệu:
def read_million_en(A, n):
    ans = ""
    sohangtrieu = n // 1000000
    sohangngan = n % 1000000
    if count_number(sohangtrieu) == 2:
        ans = read_2_en(A, sohangtrieu) + " million" +  read_thousand_2_en(A, sohangngan)
    elif count_number(sohangtrieu) == 3:
        ans = read_3_1_en(A, sohangtrieu) + " million" + read_thousand_2_en(A, sohangngan)
    elif sohangtrieu < 10 and sohangtrieu > 0:
        ans = A[sohangtrieu][0] + " million" + read_thousand_2_en(A, sohangngan)
    elif sohangtrieu == 0:
        ans = read_thousand_en(A, sohangngan)
    return ans


def read_million_2_en(A, n):
    ans = []
    sohangtrieu = n // 1000000
    sohangngan = n % 1000000
    if sohangtrieu == 0:
        ans = read_thousand_2_en(A, sohangngan)
    elif sohangtrieu < 10 and sohangtrieu > 0:
        ans = ', ' + A[sohangtrieu][0] + " million" + read_thousand_2_en(A, sohangngan)
    elif sohangtrieu < 100:
        ans = ', ' + read_3_2_en(A, sohangtrieu) + " million" + read_thousand_2_en(A, sohangngan)
    else:
        ans =  ', ' + read_million_en(A, n)
    return ans


# Đọc số hàng tỉ:
def read_billion_en(A, n):
    ans = ""
    sohangty = n // 1000000000
    sohangtrieu = n % 1000000000
    if count_number(sohangty) == 2:
        ans = read_2_en(A, sohangty) + " billion" + read_million_2_en(A, sohangtrieu)
    elif count_number(sohangty) == 3:
        ans = read_3_1_en(A, sohangty) + " billion" + read_million_2_en(A, sohangtrieu)
    elif sohangty < 10 and sohangty > 0:
        ans = A[sohangty][0] + " billion" + read_million_2_en(A, sohangtrieu)
    elif sohangty == 0:
        ans = read_million_en(A, sohangtrieu)
    return ans
#Hàm tổng:
def integer_to_english_numeral(n, activate_tts = False):

    if not isinstance(n, int):
        raise TypeError("Not an integer.")
    if n < 0:
        raise ValueError("Not positive integer.")
    if n > 999999999999:
        raise OverflowError
    if n <= 10:
        result_en = A[n][0]
    elif n > 10 and n < 100:
        result_en = read_2_en(A, n)
    else:
        result_en = read_billion_en(A, n)
    if activate_tts == True:
        replace = result_en.replace("-", " ")
        replace1 = replace.replace(",", " ")
        for i in replace1.split():
            for k in A:
                if i == k[0]:
                    sound = pygame.mixer.Sound(k[1])
                    sound.play()
                    pygame.time.wait(1000)

    elif activate_tts != "" and not isinstance(activate_tts, bool):
        raise TypeError
    return result_en


#Nhập số n:
n = int(input("Enter n :"))
#Chon kieu doc theo tieng Viet hay tieng Anh?
choose=input("Enter E to choose english or V to choose vietnamese: ")
a = input("Do you want to activate Text-to-speech? (True or False ?)") #Nhap cau hoi co muon kich hoat che do text to speech?
if a == "True" or a == "true":
    activate_tts = True                 #Chuyen doi cau tra loi sang kieu ky tu Boolean
elif a == "False" or a == "false":
    activate_tts = False
else:
    activate_tts = a                    #Neu cau tra loi khong phai la True /False, du lieu se khong chuyen doi ve kieu Boolean va raise TypeError
if choose=="E" or choose == 'e':
    print(integer_to_english_numeral(n, activate_tts))
elif choose =='V' or choose =='v':
    # Nhập region:
    region = input("Enter region: ")
    print(integer_to_vietnamese_numeral(n, region, activate_tts))

