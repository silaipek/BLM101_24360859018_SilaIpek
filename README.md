# BLM101_24360859018_SilaIpek

# Öğrenci Bilgileri
-Ad Soyad: Sıla İpek
-Öğrenci numarası:24360859018
-Bölüm:Bilgisayar Mühendisliği
-Ders: BLM101 – Bilgisayar Mühendisliğine Giriş

---

# Brookshear Makine Dili Yorumlayıcısı (Decoder)

## Proje Ne Hakkında?
Projemin konusu, kullanıcıdan 4 haneli makine kodu alıp bunu parçalara ayırmak ve Appendix C tablosundaki kurallara göre ne işe yaradıklarını ekrana yazdırmak.


# Kodun Mantığı

## Kod Ne Yapıyor?
-Program kullanıcıdan 4 haneli bir komut istiyor ve bu komutu
- **Op-code**
- **Kaydedici (Register)**
- **Operand (Adres veya Değer)**
olacak şekilde parçalara ayırıyor. 
Daha sonra Appendix C tablosuna göre ilgili komutun ne yaptığı kullanıcıya Türkçe bir açıklama ile gösteriyor.

## Nasıl Çalıştırılır?
- Bilgisayarınızda Python 3 yüklü olması yeterlidir.
- Herhangi bir kurulum gerektirmez.
- Terminale `python [dosya_adi].py` yazarak direkt çalıştırabilirsiniz.
- Çıkmak istediğinizde kod yerine `X` yazmanız yeterli.

## Programda Kullanılanlar:

input() → kullanıcıdan veri almak için

print() → ekrana yazı yazdırmak için

while, if-elif, for → temel kontrol yapıları

.upper() → yazıyı büyük harfe çevirmek için

Bunların hiçbiri kütüphane değildir, Python’un temel yapılarıdır.
  
## Programın Çalışma Mantığı

**1.Giriş ve Kontrol** : Programın sürekli çalışması için bir while döngüsü  kullandım. Önce kullanıcıdan HEX kodunu alıyorum. `upper()` kullanarak harfleri büyütüyorum(Kullanıcıdan veri alırken çok fazla hata olmaması için). Eğer kod 4 hane değilse veya içinde G,P gibi HEX olmayan harfler varsa program hata verip tekrar soruyor.

**2.Kod Parçalama**: Gelen 4 haneli kodu 
     -`opcode`: İlk hane (Yapılacak işlem).
    - `register`: İkinci hane (Kullanılan kaydedici).
    - `operand`: Son iki hane (Adres veya değer).
    
**3.Komut Seçimi**: "if-elif" yapısını kullanarak tablodaki tüm komutları (1'den C'ye kadar) tanımladım. Parçalanan opcode hangi duruma uyuyorsa, program ekrana o komutun Türkçe olarak açıklamasını yazdırıyor.
## Örnek
-**Kullanıcı Girdisi:** :`20A3`
-**Programın Çıktısı:** :"Değeri A3 olan bit desenini, 0 numaralı kaydediciye (Register) yukle."

**4.Bitiş**:Kullanıcı "x" veya "X" girince program çalışmayı durdurur.











