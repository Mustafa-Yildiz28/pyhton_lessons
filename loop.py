sifre = "1234"
hak = 3
loop = 0

while loop < hak:
    giris = input("Şifreyi giriniz: ")
    if giris == sifre:
        print("Giriş başarılı!")
        break
    else:
        print("Hatalı giriş!")
        loop += 1
else:
    # break çalışmadan döngü hak bittiği için sonlanırsa burası çalışır
    print("Deneme hakkınız bitti.")