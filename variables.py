# 1. DEĞİŞKENLER VE VERİ TİPLERİ (Variables & Data Types)
"""
musteri_adi = "Elif"          # str (metin)
kahve_adedi = 2                # int (tam sayı)
birim_fiyat = 85.50            # float (ondalıklı sayı)
ogrenci_mi = True              # bool (mantıksal değer: True / False)
hediye_kuponu = None           # NoneType (şu an bir kupon yok)

# 2. TİPLERİ KONTROL ETME
print("--- Değişkenlerin Veri Tipleri ---")
print("musteri_adi tipi :", type(musteri_adi))
print("kahve_adedi tipi :", type(kahve_adedi))
print("birim_fiyat tipi :", type(birim_fiyat))
print("ogrenci_mi tipi  :", type(ogrenci_mi))
print()

# 3. İŞLEMLER VE MATEMATİKSEL HESAPLAMA
toplam_tutar = kahve_adedi * birim_fiyat   # int ile float çarpımı -> float olur

# 4. TİP DÖNÜŞÜMÜ (Type Casting)
# Kullanıcıya mesaj gösterirken sayıları metne (str) çevirip birleştirebiliriz
# ya da modern yöntem olan 'f-string' kullanabiliriz:

print("--- Sipariş Özeti ---")
print(f"Müşteri: {musteri_adi}")
print(f"Alınan Kahve: {kahve_adedi} adet")
print(f"Toplam Borç: {toplam_tutar} TL")
print(f"Öğrenci İndirimi Geçerli mi?: {ogrenci_mi}")

# Ondalıklı tutarı tam sayıya yuvarlamadan dönüştürme (küsuratı atma)
tam_tutar = int(toplam_tutar)
print(f"Küsuratsız (int) Tutar: {tam_tutar} TL (tipi: {type(tam_tutar)})")  """

# -----------------------------MY HOMEWORK-------------------------------------
film_adi="Dune"
kiralama_gunu= 30
gunluk_ucret=43.50
vip_uye_mi=True
yorum=None

print("film_adi:" ,type(film_adi))
print("kiralama_gunu:" ,type(kiralama_gunu))
print("gunluk_ucret:" ,type(gunluk_ucret))
print("vip_uye_mi:" ,type(vip_uye_mi))
print("yorum:" ,type(yorum))

toplam_ucret=kiralama_gunu * gunluk_ucret
yuvarlanmis_ucret=int(toplam_ucret)

print("-----ÖZET-----")
print(f"Film: {film_adi}")
print(f"Kiralama Günü: {kiralama_gunu} gün")
print(f"Günlük Ücret: {gunluk_ucret} TL")
print(f"VIP Üye mi?: {vip_uye_mi}")
print(f"Yorum: {yorum}")
print(f"Toplam Tutar: {toplam_ucret} TL")
print(f"Yuvarlanmış Tutar: {yuvarlanmis_ucret} TL")