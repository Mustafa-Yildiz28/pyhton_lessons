"""
# Sözlük oluşturma (Key: Coin adı, Value: Fiyatı)
portfoy = {
    "BTC": 92000,
    "ETH": 3100,
    "AVAX": 35
}
# 1. Veriye erişim (Anahtar adını vererek değeri alma)
print("BTC Fiyatı:", portfoy["BTC"])

# 2. Yeni veri ekleme
portfoy["SOL"] = 210

# 3. Mevcut veriyi güncelleme (Anahtar zaten varsa değeri günceller)
portfoy["AVAX"] = 42

# 4. Veri silme
del portfoy["ETH"]

# 5. Sözlük üzerinde döngüyle gezinme (.items() hem anahtarı hem değeri verir)
print("\n--- Güncel Portföy ---")
for coin, fiyat in portfoy.items():
    print(f"{coin}: ${fiyat}")
    """
oyuncu={
    "isim": "Marco Asensio",
    "gol": 14 ,
    "takim": "Fenerbahçe"
}
print(oyuncu["takim"])
oyuncu["gol"]=15
oyuncu["asist"]=16
for x,y in oyuncu.items():
    print (f"{x}: {y}" )