"""
kullanici_adi = input("Adiniz: ")
yas = int(input("Yasiniz: "))
sehir = input("Sehriniz: ")
sayi = 10
Sayi = 20
if yas >= 18:
	durum = "yetiskin"
else:
	durum = "cocuk"
mesaj = (
	kullanici_adi + " - " + durum
)
print(mesaj)
print("Sehir:", sehir, "sayi:", sayi, "Sayi:", Sayi)
print("Buyuk harfli isim:", kullanici_adi.upper())
"""
isim=input("Adiniz: ")
yas=int(input("Yasiniz: "))
bilet=50;
Bilet=100;
if yas>=65:
    print(isim +" bilet ücretin: " + str(bilet))
else:
    print(isim +" bilet ücretin: " + str(Bilet))