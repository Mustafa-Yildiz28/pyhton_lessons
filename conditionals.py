"""
# Kullanıcı bilgileri
yas = 20
ogrenci_mi = True
gun = "Çarşamba"

# --- 1. if - elif - else ile Fiyat Belirleme ---
if yas < 7:
    bilet_fiyati = 0
    print("Çocuklar için bilet ücretsiz!")
elif yas >= 65:
    bilet_fiyati = 60
    print("65 yaş üstü indirimli bilet.")
elif ogrenci_mi and yas < 25:
    bilet_fiyati = 80
    print("Öğrenci indirimi uygulandı.")
else:
    bilet_fiyati = 120
    print("Tam bilet uygulandı.")

# --- 2. Gün Kontrolü (Ek İndirim) ---
if gun.lower() == "çarşamba":
    print("Halk günü indirimi: Bilet fiyatından 10 TL düşülüyor.")
    bilet_fiyati -= 10

print(f"Ödemeniz gereken tutar: {bilet_fiyati} TL\n")

# --- 3. match-case Yapısı ile Salon Seçimi ---
salon_kodu = "IMAX"

match salon_kodu:
    case "IMAX":
        print("Büyük ekran ve surround ses salonu seçildi.")
    case "3D":
        print("3D gözlüklerinizi girişte almayı unutmayın.")
    case "STANDART":
        print("Standart salon seçildi.")
    case _:  # else gibi, hiçbirine uymazsa
        print("Bilinmeyen salon tipi!")
        """

vize = 60
final = 75
devamsizlik_gun = 4
ortalama=(vize*0.4)+(final*0.6)
sonuc=None
harf_notu=None
if devamsizlik_gun> 5:
    print("Devamsızlıktan Kaldınız (Harf Notu: NA)")
    sonuc= "Kaldi"
    harf_notu="NA"
else:
    if ortalama >= 85:
        print("Tebrikler, geçtiniz.Harf notunuz: AA")
        sonuc= "Gecti"
        harf_notu="AA"
    elif ortalama >= 70 and ortalama <85:
        print("Tebrikler, geçtiniz.Harf notunuz: BB")
        sonuc= "Gecti"
        harf_notu="BB"
    elif ortalama >= 50 and ortalama <70:
        print("Tebrikler, geçtiniz.Harf notunuz: CC")
        sonuc= "Gecti"
        harf_notu="CC"
    elif ortalama < 50:
        print("Harf notunuz: FF .Maalesef kaldiniz")
        sonuc= "Kaldi"
        harf_notu="FF"
print(f"Ortalama Not: {ortalama}")        
print(f"Sonuç Durumu: {sonuc}")     
print(f"Harf Notu: {harf_notu}")   



    
