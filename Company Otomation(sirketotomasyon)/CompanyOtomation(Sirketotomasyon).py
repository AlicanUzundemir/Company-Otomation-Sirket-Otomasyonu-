#SQL VERİ TABANI KULLANARAK YAZARAK DAHA KOLAY OLUR AMA TEXT SAYFASI KULLANICAZ.
class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calisanlarEkle()
        if secim == 2:
            self.calisanlarCikar()
        if secim == 3:
            ay_yil_secim = input("Yillik bazda gormek istermisiniz? (e/h)")
            if ay_yil_secim == "e":
                self.verilecekMaasGoster(hesap="y")
            else:
                self.verilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGir
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        secim = int(input("***** {} Otomasyonuna hoş geldiniz ****\n\n1-Calisan Ekle\n2-Calisan Cikar \n3-Verilecek Maas Goster \n4-Maaslari ver\n5-Masraflari gir \n6-Gelir gir \n\nSeciminizi giriniz: ".format(self.ad)))
        while secim < 1 or secim > 6:
            secim = int(input("Lutfen 1 - 6 arasında belirtilen seceneklerden giriniz!"))

        return secim

    def calisanlarEkle(self):
        id = 1
        ad = input("Calisanin adini giriniz: ")
        soyad = input("Calisanin soyadii giriniz: ")
        yas = input("Calisanin yasini giriniz: ")
        cinsiyet = input("Calisanin cinsiyetini giriniz: ")
        maas = input("Calisanin maasini giriniz: ")

        with open("calisanlar.txt","r") as dosya:
            calisanListesi = dosya.readline()
        if len(calisanListesi) == 0:
            id = 1
        else:
            with open("calisanlar.txt","r") as dosya:
                id= int(dosya.readlines()[-1].split(")")[0]) + 1


        with open("Calisanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
                    


    def calisanlarCikar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        
        gCalisanlar = []

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))
        
        for calisan in gCalisanlar:
            print(calisan)

        secim = int(input("Lutfen cikarmak istediginiz calisanin numarasini giriniz(1-{}: ".format(len(gCalisanlar))))
        while secim < 1 or secim >len(gCalisanlar):
            secim = int(input("Lutfen (1-{}) arasinda numara giriniz: ".format(len(gCalisanlar))))

        calisanlar.pop(secim-1)

        sayac = 1

        dCalisanlar = []

        for calisan in calisanlar:
            dCalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac +=1

        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(dCalisanlar)


    def verilecekMaasGoster(self,hesap = "a"):
        """ hesap: a ise aylik,y ise yillik hesap"""
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        if hesap == "a":
            print("Bu at toplam vermeniz gereken maas: {}".format(sum(maaslar)))
        else:
            print("Bu ay toplam vermeniz gereken maas: {}".format(sum(maaslar)*12))

        


    def maaslariVer(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        toplamMaas = sum(maaslar)

        #### bütceden maas alma ####

        with open("butce.txt","r") as dosya:
            tbutce = int(dosya.readlines()[0])

        tbutce = tbutce - toplamMaas

        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))

    def masrafGir(self):
        pass

    def gelirGir(self):
        pass



Sirket = Sirket("AU Bilism sireketi")

while Sirket.calisma:
    Sirket.program()
