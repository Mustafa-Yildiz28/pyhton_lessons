"""
# 1. Implicit (Otomatik) Dönüşüm
tam_sayi = 10          # int
ondalikli = 2.5        # float
sonuc = tam_sayi + ondalikli
print("Otomatik sonuç:", sonuc, "| Tipi:", type(sonuc)) # Python otomatik float yaptı

# 2. Explicit (Manuel) Dönüşüm - String'den Sayıya


kripto_fiyat_str = "92500.50"  # API'den veya input'tan gelen veri genelde str olur
adet_str = "2"

# Matematiksel işlem için dönüştürme şart (yoksa metinleri yan yana yapıştırır)
fiyat = float(kripto_fiyat_str)
adet = int(adet_str)
toplam_tutar = fiyat * adet
print("Toplam Tutar:", toplam_tutar)

# 3. Sayıdan String'e Dönüşüm (Metin birleştirme için)
bakiye = 1500
# print("Bakiyeniz: " + bakiye) -> HATA VERİR! Çünkü str ile int '+' ile toplanamaz.
mesaj = "Güncel Bakiyeniz: " + str(bakiye) + " TL"
print(mesaj)

# 4. Float'tan Int'e Dönüşüm (Dikkat: Yuvarlamaz, virgülden sonrasını direkt keser!)
pi = 3.99
print("Int hali:", int(pi)) # Çıktı 4 değil, 3 olur
"""
not1=float(input("İlk notunuzu giriniz: "))
not2=float(input("İkinci notunuzu giriniz: "))
ortalama=(not1+not2)/2
tam_ortalama=int(ortalama)
mesaj="Ortalamanız: " + str(ortalama), "Tam sayı karşılığı: " + str(tam_ortalama)
print(mesaj)