"""50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin
inputlarla girilen doğru yanlış sayısına göre aldığı puanı
hesaplayan programı yazınız. Ogrenci sınıfı diye bir sınıf tanımlanacak.
Bu sınıfın içinde ogrenciAdı, ogrenciSoyadı, ogrenciSınıf’ı değişkenleri bulunacak.
Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecek.  Soru diye bir sınıfınız olacak.
Bu sınıfın NetSayısı(...) ve Hesapla(...) diye iki fonksiyon olacak.
NetSayısı fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulur.
Hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacak. Her net 2 puan.
En sonunda öğrenci bilgileri ve puanı console gösterilecek."""


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
