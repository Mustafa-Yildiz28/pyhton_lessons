"""
# 1. Liste oluşturma
envanter = ["Kiliç", "Kalkan", "Can İksiri"]

# 2. Yeni eşya ekleme (sona ekler)
envanter.append("Harita")

# 3. İndeks kullanarak eleman değiştirme (Kalkan yerine Zırh koyalım)
envanter[1] = "Çelik Zirh"

# 4. Belirli bir eşyayı silme
envanter.remove("Can İksiri")

# 5. Sonuçları ekrana yazdırma
print("Güncel Envanter:", envanter)
print("İlk Eşya:", envanter[0])
print("Toplam Eşya Sayisi:", len(envanter))
"""

fiyatlar=[100,200,500,300]
fiyatlar.append(200)
fiyatlar[1]=250
less=fiyatlar[0]
for  fiyat in (fiyatlar):
    if fiyat< less:
        less=fiyat
fiyatlar.remove(less)
print(fiyatlar)
print(fiyatlar[-1])
print(sum(fiyatlar))

