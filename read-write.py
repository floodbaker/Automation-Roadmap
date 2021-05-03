"""sayiAtama ve sayiOkusu isimli 2 tane fonksiyon tanımlayın
bu fonksiyonlardan sayiAtama fonksiyonu 2 basamaklı bi sayiyı
parametre olarak alabilecek ve fonksiyon içinde bu değer bir değişkene atanacak.
Daha sonra sayiAtama fonksiyonu içinde sayiOkunusu isimli fonksiyon çağırılarak
değişkene atanan sayinın okunuşu string olarak verilecek. sayiAtama fonksiyonu
2 basamaktan az yada daha fazla sayiyı kabul etmeyecek. """

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