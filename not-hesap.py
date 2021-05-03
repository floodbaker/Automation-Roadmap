while True:
    vize1 = int(input("Vize-1 değerini giriniz: "))
    if vize1 > 100 or vize1 < 0:
        print(f"{vize1} olarak girdiğiniz vize-1 değeri 0-100 arasında değildir.\n"
              f"Lütfen 0-100 arasında bir değer giriniz.")
        continue

    vize2 = int(input("Vize-2 değerini giriniz: "))
    if vize2 > 100 or vize2 < 0:
        print(f"{vize2} olarak girdiğiniz vize-2 değeri 0-100 arasında değildir.\n"
              f"Lütfen 0-100 arasında bir değer giriniz.")
        continue

    final = int(input("Final değerini giriniz: "))
    if 0 > final > 100:
        print(f"{final} olarak girdiğiniz vize-2 değeri 0-100 arasında değildir.\n"
              f"Lütfen 0-100 arasında bir değer giriniz.")
        continue

    total = (vize1 * 30 / 100) + (vize2 * 30 / 100) + (final * 40 / 100)
    print(f"\nVize-1 Değeriniz: {vize1}\n"
          f"Vize-2 Değeriniz: {vize2}\n"
          f"Final Değeriniz: {final}\n"
          f"Genel Ortalamanız: {total}")
    if 90 <= total <= 100:
        print("Harf Notunuz: AA")
    elif 85 <= total < 90:
        print("Harf Notunuz: BA")
    elif 80 <= total < 85:
        print("Harf Notunuz: BB")
    elif 75 <= total < 80:
        print("Harf Notunuz: CB")
    elif 70 <= total < 75:
        print("Harf Notunuz: CC")
    elif 65 <= total < 70:
        print("Harf Notunuz: DC")
    elif 60 <= total < 65:
        print("Harf Notunuz: DD")
    elif 55 <= total < 60:
        print("Harf Notunuz: FD")
    elif 0 <= total < 55:
        print("Harf Notunuz: FF")

    break


