# Brookshear Makine Dili Yorumlayıcısı (Decoder)
# Bu proje, girilen 4 haneli HEX kodlarını analiz ederek
# Appendix C tablosuna göre Türkçe açıklamasını yapar.

print(" === Brookshear Makine Dili Yorumlayici===")

while True:
    #Kullanicidan girdi al 
     #upper() fonksiyonu kullanıcının girdiği koddaki harfleri büyük harfe çevirir.
    kod = input("4 haneli HEX kodu giriniz (Cikmak icin x): ").upper()

    # Çıkış kontrolü
    if kod == "X":
        print("Programdan cikiliyor...")
        break

    # Uzunluk kontrolü
    if len(kod) != 4:
        print("Hata: Kod 4 haneli olmalidir.")
        continue

    # Geçersiz karakter kontrolü (HEX dışında karakter girilemez)
    hex_karakterler = "0123456789ABCDEF"
    hatali = False

    for harf in kod:
        if harf not in hex_karakterler:
            hatali = True

    if hatali:
        print("Hata! Gecersiz HEX karakteri girdiniz (0-9 veya A-F arasi olmali)")
        continue

    # Kod parcalama islemleri
    #Örnek: 2F0A --> Opcode:2, Kaydedici:F, Operand:0A
    opcode = kod[0]
    register = kod[1]
    operand = kod[2] + kod[3]

    # Komutlar
    if opcode == "1":
        print(operand, "adresindeki bellek hucresinin icerigini",
              register, "numarali kaydediciye (Register) yukle.")

    elif opcode == "2":
        print("Degeri", operand, "olan bit desenini,", 
              register, "numarali kaydediciye (Register) yukle.")
        
    elif opcode == "3":
        print(register, "numarali kaydedicideki (Register) veriyi,", 
              operand, "adresindeki bellek hucresine kaydet.")

    elif opcode == "4":
        print(register, "numarali kaydedicideki veriyi,", 
              operand[0], "numarali kaydediciye (Register) kopyala.")

    elif opcode == "5":
        print(operand[0], "ve", operand[1],
              "numarali kaydedicilerdeki sayilari topla,sonucu",
              register,"numarali kaydediciye (Register) yaz.")

    elif opcode == "6":
        print(operand[0], "ve", operand[1],
              "numarali kaydedicilerdeki ondalikli sayilari topla, sonucu", 
              register, "numarali kaydediciye (Register) yaz.")

    elif opcode == "7":
        print(operand[0], "ve", operand[1],
           "numarali kaydedicilerinde OR (VEYA) işlemi yap, sonucu", 
              register, "numarali kaydediciye (Register) yaz.")   

    elif opcode == "8":
        print(operand[0], "ve", operand[1],
            "numarali kaydedicilerinde AND (VE) işlemi yap, sonucu", 
              register, "numarali kaydediciye (Register) yaz.")  

    elif opcode == "9":
        print(operand[0], "ve", operand[1],
            "numarali kaydedicilerinde XOR (Özel VEYA) işlemi yap, sonucu", 
              register, "numarali kaydediciye (Register) yaz.")  

    elif opcode == "A":
        print(register, "numarali kaydedicideki (Register) veriyi saga dogru",
              operand[1], "kez dondur.")

    elif opcode == "B":
        print("Eger 0 numarali kaydedici ile", register, 
              "numarali kaydedici (Register) eşitse,", 
              operand, "adresine atla.")

    elif opcode == "C":
        print("Programin calismasini durdur (HALT).")

    else:
        print("Tanimlanmamis bir Op-code girdiniz.")

