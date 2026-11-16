"""
# Tekrar eden elemanların otomatik silinmesi
sayilar = {1, 2, 2, 3, 4, 4, 5}
print("Tekrarsız küme:", sayilar)  # Çıktı: {1, 2, 3, 4, 5}

# Eleman ekleme ve silme
sayilar.add(6)
sayilar.discard(2)

# İki grup arasındaki ortak ve farklı kişileri bulma
python_bilenler = {"Ali", "Ayşe", "Mehmet", "Zeynep"}
sql_bilenler = {"Mehmet", "Zeynep", "Can", "Ece"}

# Her iki dili de bilenler (Kesişim)
ortak = python_bilenler & sql_bilenler
print("İkisini de bilenler:", ortak)

# Sadece Python bilenler (Fark)
sadece_python = python_bilenler - sql_bilenler
print("Sadece Python bilenler:", sadece_python)
"""


cumartesi_katilimcilari={"Ahmet", "Mehmet", "Ayşe", "Ahmet", "Fatma", "Can"}
pazar_katilimcilari={"Ayşe", "Can", "Zeynep", "Burak", "Zeynep"}
iki_günede_katilanlar= cumartesi_katilimcilari & pazar_katilimcilari
print(iki_günede_katilanlar)
sadece_pazara_katilanlar= pazar_katilimcilari -cumartesi_katilimcilari
print(sadece_pazara_katilanlar)
pazar_katilimcilari.add("Emre")
print(pazar_katilimcilari)