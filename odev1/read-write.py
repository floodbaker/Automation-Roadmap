sayi = int(input("Okunuşunu öğrenmek istediğiniz sayıyı giriniz: "))


def sayiAtama(gelen_sayi):
    digits = 0
    gonderilecek_sayi = gelen_sayi
    while gelen_sayi > 0:
        digits = digits + 1
        gelen_sayi = gelen_sayi // 10
    if digits != 2:
        return exit('HATA! Lütfen 2 basamaklı bir sayı ile tekrar deneyiniz.')
    sayiOkunusu(gonderilecek_sayi)


def sayiOkunusu(count):
    birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    birinci = count % 10
    ikinci = count // 10
    print("Sayının okunuşu: ", onlar[ikinci] + " " + birler[birinci])

sayiAtama(sayi)
