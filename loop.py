sifre="1234"
hak=3
loop=0
while loop<hak :
    giris=input("Şifreyi giriniz:")
    if giris==sifre:
        print("giriş başarili")
        break
    else:
        loop=loop+1
        print("Hatali şifre.")