class personel:
    def __init__(self, adı, soyadı, yaşı, çalıştığı_bölüm, işe_başlama_yılı, maaşı):
        self.adı = adı
        self.soyadı = soyadı
        self.yaşı = yaşı
        self.çalıştığı_bölüm = çalıştığı_bölüm
        self.işe_başlama_yılı = işe_başlama_yılı
        self.maaşı = maaşı

class firma:
    def __init__(self):
        self.personelListesi = []

    def personel_ekle(self, personel):
        self.personelListesi.append(personel)

    def personel_listele(self):
        for index, personel in enumerate(self.personelListesi, 1):
            print("\n")
            print("{}. personel".format(index))
            print("Adı:", personel.adı)
            print("Soyadı:", personel.soyadı)
            print("Yaşı:", personel.yaşı)
            print("Çalıştığı Bölüm:", personel.çalıştığı_bölüm)
            print("İşe Başlama Yılı:", personel.işe_başlama_yılı)
            print("Maaşı:", personel.maaşı)

    def maas_zammi(self, personel_index, zam_orani):
        personel = self.personelListesi[personel_index - 1]
        personel.maaşı *= (1 + zam_orani / 100)

    def personel_cikart(self, personel_index):
        del self.personelListesi[personel_index - 1]


if __name__ == "__main__":
    sirket = firma()

    while True:
        print("\n----------MENÜ------------\n")
        print("1 - Personel Ekle")
        print("2 - Personelleri Listele")
        print("3 - Maaş Zammı Yap")
        print("4 - Personeli Sil")
        print("5 - Çıkış")
        secim = int(input("Yapmak istediğiniz işlemi seçin: "))

        if secim == 1:
            adi = input("Personelin Adı: ")
            soyadi = input("Personelin Soyadı: ")
            yasi = int(input("Personelin Yaşı: "))
            bolumu = input("Çalıştığı Bölüm: ")
            baslama_yili = int(input("İşe Başlama Yılı: "))
            maasi = float(input("Personelin Maaşı: "))

            yeni_personel = personel(adi, soyadi, yasi, bolumu, baslama_yili, maasi)
            sirket.personel_ekle(yeni_personel)

        elif secim == 2:
            sirket.personel_listele()

        elif secim == 3:
            sirket.personel_listele()
            personel_index = int(input("Maaş zammı yapılacak personelin numarasını girin: "))
            zam_orani = float(input("Maaş artış oranını girin (%): "))
            sirket.maas_zammi(personel_index, zam_orani)

        elif secim == 4:
            sirket.personel_listele()
            personel_index = int(input("Silinecek personelin numarasını girin: "))
            sirket.personel_cikart(personel_index)

        elif secim == 5:
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
