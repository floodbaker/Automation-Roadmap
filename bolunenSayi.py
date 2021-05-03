def bolunenSayi(min, max, bol):
    sonuc = []
    adet = 0
    if min > 0 and max > 0 and bol > 0:
        if(max>min):
            for min in range(min, max):
                if min % bol == 0:
                    sonuc.append(min)
                    adet +=1
            print(sonuc)
            print("Bölünen toplam sayı: ",adet)
        else:
            print(f"{min} olarak girilen minimum değer,"
                  f"{max} olarak girilen maximum değerden büyük olamaz.")
    else:
        print("Minimum, maximum ve bolunecek sayı değerleri negatif olamaz!")
    if len(sonuc) == 0:
        print(f"Aralıktaki hiçbir sayı {bol} değerine tam bölünemiyor")


min_sayi = int(input("Minimum sayiyi giriniz. "))
max_sayi = int(input("Maximum sayiyi giriniz. "))
bolunecek_sayi = int(input("Bolunecek sayiyi giriniz. "))

bolunenSayi(min_sayi, max_sayi, bolunecek_sayi)
