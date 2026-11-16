"""
# Tanımlama
koordinat = (41.0082, 28.9784)

# Elemana erişme ve döngüyle gezme (Listelerle birebir aynı)
print(koordinat[0]) # Çıktı: 41.0082

for deger in koordinat:
    print(deger)

# Unpacking (Paketten çıkarma - Çok sık kullanılır)
enlem, boylam = koordinat
print(enlem) # Çıktı: 41.0082

# HATA VERİR (Değiştirilemez):
# koordinat[0] = 40.0  -> TypeError hatası alırsın!
"""
sepet=[("klavye",1,100),("mouse",3,50),("hopörler",2,250)]
toplam=0
for esya, adet, ücret in sepet:
    print("Eşya: ", esya,"Adet: ",adet,"Ücret: ",ücret)
    toplam=toplam+(adet*ücret)
print("Toplam ücret: " , toplam)