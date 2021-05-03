class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ad = ogrenciAdi
        self.soyad = ogrenciSoyadi
        self.sinif = ogrenciSinifi


class Soru:
    def netSayisi(self, dogru_sayisi, yanlis_sayisi):
        net = dogru_sayisi - yanlis_sayisi / 4
        return net

    def hesapla(self, net):
        puan = net * 2
        return puan


ogrenci = Ogrenci("Açelya", "Demirci", "BLM322")
soru = Soru()

dogru = int(input("Dogru sayisini giriniz. "))
yanlis = int(input("Yanlis sayisini giriniz. "))

print("Öğrenci Bilgileri"
      "\nAdı: ", ogrenci.ad,
      "\nSoyadı: ", ogrenci.soyad,
      "\nSınıfı: ", ogrenci.sinif)

if dogru + yanlis <= 50:
    print("Ogrenci Neti:", soru.netSayisi(dogru, yanlis))
    print("Ogrenci Puanı:", soru.hesapla(net=soru.netSayisi(dogru, yanlis)))
else:
    print("Doğru ve yanlış sayılarınızın toplamı 50'yi geçmemeli, tekrar deneyiniz.")
