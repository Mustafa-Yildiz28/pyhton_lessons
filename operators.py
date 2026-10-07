"""
bakiye = 1000
sepet_tutari = 250
kargo_ucreti = 40
vip_uye = True

# 1. Aritmetik & Atama
toplam_odeme = sepet_tutari + kargo_ucreti
bakiye -= toplam_odeme  # Bakiyeden toplam ödemeyi düş (bakiye = bakiye - toplam_odeme)

# 2. Karşılaştırma & Mantıksal
yeterli_bakiye_var_mi = bakiye >= 0
ucretsiz_kargo_hakki = vip_uye or (sepet_tutari > 300)

print(f"Toplam Ödeme: {toplam_odeme} TL")
print(f"Kalan Bakiye: {bakiye} TL")
print(f"İşlem Başarılı mı?: {yeterli_bakiye_var_mi}")
print(f"Ücretsiz Kargo Kazanıldı mı?: {ucretsiz_kargo_hakki}")

# 3. Kalan Bulma (Modül)
kalan_para_cift_mi = (bakiye % 2) == 0
print(f"Kalan bakiye çift sayı mı?: {kalan_para_cift_mi}") """

vize = 60
final = 75
devamsizlik = 3
ortalama=(vize *0.4)+ (final * 0.6)
not_yeterli_mi= ortalama >= 50
devamsizlik_yeterli_mi=devamsizlik<=5
dersi_gecti_mi= not_yeterli_mi and devamsizlik_yeterli_mi
print(f"ortalama: {ortalama}")
if(dersi_gecti_mi):
 print("Dersi geçtiniz")
else:
 print("Dersi geçemediniz")