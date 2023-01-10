# Eda Nur MUTLU - 170421843

global ucret1  # her satıştan sonra oluşan ücret bilgisini ayrı toplamlarda saklamak için global değişkenler tanımlanmaktadır
ucret1 = 0
global ucret2
ucret2 = 0
global ucret3
ucret3 = 0
global ucret4
ucret4 = 0


def ana_menu():
    print("==============================RESTART==============================")
    print(
        "************\n"
        "**ANA MENÜ**\n"
        "************\n"
        "************\n"
        "1.Rezervasyon\n"
        "2.Salonu yazdır\n"
        "3.Yeni etkinlik\n"
        "4.Toplam Ciro\n"
        "0.Çıkış\n"
        "************")
    while True:
        try:  # kullanıcı tarafından girilen veriler try-except yapısı ile kontrol edilmektedir
            secim = int(input("Seçiminiz ? "))
        except:
            print("Geçersiz sayı girdiniz!")
        else:
            if secim < 0 or secim > 4:
                print("Lütfen 0-4 arasında bir sayı giriniz!")
            else:
                break

    if secim == 1:
        rezervasyon(koltuk)
    elif secim == 2:
        salonu_yazdir(koltuk) 
    elif secim == 3:
        salon_olustur()  # yeni etkinlik için yeni bir salon oluşturulmaktadır
        ana_menu()
    elif secim == 4:
        toplam_ciro()
        ana_menu()
    elif secim == 0:
        exit()    # sistemden çıkış yapılmaktadır
    else:
        print("\nYanlış tuşlama yaptınız!\n")
        ana_menu()


def rezervasyon(koltuk):
    global ucret1
    global ucret2
    global ucret3
    global ucret4

    while True:
        try:  # kullanıcı tarafından girilen veriler try-except yapısı ile kontrol edilmektedir
            kategori = int(input("Kategori (1-4) ? "))
        except:
            print("Geçersiz sayı girdiniz!")
        else:
            if kategori < 1 or kategori > 4:
                print("Lütfen 1-4 arasında bir sayı giriniz!")
            else:
                break

    while True:
        try:  # kullanıcı tarafından girilen veriler try-except yapısı ile kontrol edilmektedir
            bilet_adet = int(input("Bilet adedi (1-10) ? "))
        except:
            print("Geçersiz sayı girdiniz!")
        else:
            if bilet_adet < 1 or bilet_adet > 10:
                print("Lütfen 1-10 arasında bir sayı giriniz!")
            else:
                break

    if kategori == 1:
        if kalan_koltuk[0] == 0 or bilet_adet > kalan_koltuk[0]:
            print("1. kategoride ", bilet_adet, "kadar boş koltuk bulunmadığından işleminiz reddedilmiştir.\n")
            # ilgili kategorideki kalan koltuk ve girilen bilet adedi sayısına göre hata mesajı verilmektedir
        else:
            bilet_olustur(0, 10, 5, 15, bilet_adet, 0)
            fiyat1 = fiyat_hesapla(0, 0, bilet_adet)
            # her bilet satışından sonra oluşan fiyat bilgisi ayrı toplamlarda saklanmak üzere ucret1 hesaplanmaktadır
            ucret1=ucret1+fiyat1
    elif kategori == 2:
        if kalan_koltuk[1] == 0 or bilet_adet > kalan_koltuk[1]:
            print("2. kategoride ", bilet_adet, "adet boş koltuk bulunmadığından işleminiz reddedilmiştir.\n")
        else:
            bilet_olustur2(0, 10, 4, -1, 15, 20, bilet_adet, 1)
            fiyat2 = fiyat_hesapla(1, 0, bilet_adet)
            # her bilet satışından sonra oluşan fiyat bilgisi ayrı toplamlarda saklanmak üzere ucret2 hesaplanmaktadır
            ucret2=ucret2+fiyat2
    elif kategori == 3:
        if kalan_koltuk[2] == 0 or bilet_adet > kalan_koltuk[2]:
            print("3. kategoride ", bilet_adet, "adet boş koltuk bulunmadığından işleminiz reddedilmiştir.\n")
        else:
            bilet_olustur(10, 20, 5, 15, bilet_adet, 2)
            fiyat3 = fiyat_hesapla(2, 0, bilet_adet)
            # her bilet satışından sonra oluşan fiyat bilgisi ayrı toplamlarda saklanmak üzere ucret3 hesaplanmaktadır
            ucret3=ucret3+fiyat3
    elif kategori == 4:
        if kalan_koltuk[3] == 0 or bilet_adet > kalan_koltuk[3]:
            print("4. kategoride ", bilet_adet, "adet boş koltuk bulunmadığından işleminiz reddedilmiştir.\n")
        else:
            bilet_olustur2(10, 20, 4, -1, 15, 20, bilet_adet, 3)
            fiyat4 = fiyat_hesapla(3, 0, bilet_adet)
            # her bilet satışından sonra oluşan fiyat bilgisi ayrı toplamlarda saklanmak üzere ucret4 hesaplanmaktadır
            ucret4=ucret4+fiyat4
    ana_menu()


def fiyat_hesapla(n, toplam, bilet_adet):
    # fiyat_hesapla metoduna gönderilen parametreler sırasıyla:
    # (kategori no,indirimsiz toplam fiyat,bilet adedi)
    toplam = bilet_adet * ucretler[n] # ucretler[n], n+1.kategorideki bir bilet fiyatını vermektedir
    global itoplam
    itoplam = 0 # indirimli toplam fiyat tanımlaması yapılmaktadır

    # aşağıdaki if-elif yapılarında bilet adedinin indirim için gerekli aralıkta olup olmadığı kontrol edilmektedir
    if indirim[n][0] <= bilet_adet and indirim[n][1] >= bilet_adet: 
        toplam -= toplam * indirim[n][2] / 100 # indirimsiz toplam fiyat hesaplanmaktadır
        itoplam = toplam - ((toplam * indirim[n][2]) / 100) #indirim[kategori][2], yapılacak indirim oranını vermektedir
        print("\nBilet adedi: ", bilet_adet, "\nToplam tutar: ", toplam, "\nYapılan indirim: ", indirim[n][2],
              "\nNet tutar: ", itoplam)

    elif indirim[n + 1][0] <= bilet_adet and indirim[n + 1][1] >= bilet_adet:
        itoplam = toplam - ((toplam * indirim[n + 1][2]) / 100)
        print("\nBilet adedi: ", bilet_adet, "\nToplam tutar: ", toplam, "\nYapılan indirim: ", indirim[n + 1][2],
              "\nNet tutar: ", itoplam)

    elif indirim[n + 2][0] <= bilet_adet and indirim[n + 2][1] >= bilet_adet:
        itoplam = toplam - ((toplam * indirim[n + 2][2]) / 100)
        print("\nBilet adedi: ", bilet_adet, "\nToplam tutar: ", toplam, "\nYapılan indirim: ", indirim[n + 2][2],
              "\nNet tutar: ", itoplam)

    return itoplam


def toplam_ciro():
    print("1. kategori için ücret toplamı: ", ucret1) # her kategori için elde edilen ücret toplamları ekrana bastırılmaktadır
    print("2. kategori için ücret toplamı: ", ucret2)
    print("3. kategori için ücret toplamı: ", ucret3)
    print("4. kategori için ücret toplamı: ", ucret4)
    
    print("Toplam ciro: ", ucret1 + ucret2 + ucret3 + ucret4) # salonun toplam cirosu ekrana bastırılmaktadır


def bilet_olustur(h1, h2, v1, v2, bilet_adet, n):
    # bilet_olustur metoduna gönderilen parametreler sırasıyla : 
    #(başlangıç satır, bitiş satır, başlangıç sütun, bitiş sütun-1, bilet adedi, kategori no)
    print("Rezerve Edilen Koltuklar (Sira-Koltuk): ", end="")
    for i in range(h1, h2):      # satırları dönmesi için bir for kullanılmaktadır
        for j in range(v1, v2):  # sütunları dönmesi için bir for kullanılmaktadır
            if koltuk[i][j] == 1:# eğer koltuk rezerve edilmişse bu adım atlanmaktadır
                continue
            koltuk[i][j] = 1     # koltuk rezerve edilmemişse rezerve edildiği anlamına gelen 1 sayısı atanmaktadır
            bilet_adet -= 1      # rezerve edilen koltuk için bilet sayısı 1 azaltılmaktadır
            kalan_koltuk[n] -= 1 # n+1. kategorideki kalan koltuk sayısı 1 azaltılmaktadır
            print(i + 1, "-", j + 1, ", ", end="",sep="") # rezerve edilen koltuklar ekrana yazdırılmaktadır
            if bilet_adet == 0: 
                return           # girilen bilet adeti kadar rezervasyon işlemi yapıldıktan sonra metot sonlanmaktadır


def bilet_olustur2(h1, h2, v1, v2, v3, v4, bilet_adet, n):
    # bilet_olustur2 metoduna gönderilen parametreler sırasıyla : 
    #(başlangıç satır,bitiş satır,(sol)başlangıç sütun,(sol)bitiş sütun-1, (sağ)başlangıç sütun,(sağ)bitiş sütun,bilet adedi, kategori no)
    print("Rezerve Edilen Koltuklar (Sira-Koltuk): ", end="")
    for i in range(h1, h2):       # satırlar için bir for kullanılmaktadır
        for j in range(v1, v2, -1):# sol taraftaki sütunları sağdan sola doğru okumak için bir for kullanılmaktadır
            if koltuk[i][j] == 1: # eğer koltuk rezerve edilmişse bu adım atlanmaktadır
                continue
            koltuk[i][j] = 1     # koltuk rezerve edilmemişse rezerve edildiği anlamına gelen 1 sayısı atanmaktadır
            bilet_adet -= 1      # rezerve edilen koltuk için bilet sayısı 1 azaltılmaktadır
            kalan_koltuk[n] -= 1 # n+1. kategorideki kalan koltuk sayısı 1 azaltılmaktadır
            print(i + 1, "-", j + 1, ", ", end="", sep="") # rezerve edilen koltuklar ekrana yazdırılmaktadır
            if bilet_adet == 0:
                return           # girilen bilet adeti kadar rezervasyon işlemi yapıldıktan sonra metot sonlanmaktadır
        for k in range(v3, v4):  # sağ taraftaki sütunları soldan sağa doğru okumak için bir for kullanılmaktadır
            if koltuk[i][k] == 1:# eğer koltuk rezerve edilmişse bu adım atlanmaktadır
                continue
            koltuk[i][k] = 1     # koltuk rezerve edilmemişse rezerve edildiği anlamına gelen 1 sayısı atanmaktadır
            bilet_adet -= 1      # rezerve edilen koltuk için bilet sayısı 1 azaltılmaktadır
            kalan_koltuk[n] -= 1 # n+1. kategorideki kalan koltuk sayısı 1 azaltılmaktadır
            print(i + 1, "-", k + 1, ", ", end="", sep="") # rezerve edilen koltuklar ekrana yazdırılmaktadır
            if bilet_adet == 0:
                return           # girilen bilet adeti kadar rezervasyon işlemi yapıldıktan sonra metot sonlanmaktadır


def salonu_yazdir(koltuk):
    for i in range(20):
        for j in range(20):
            if koltuk[i][j] == 0:
                print("-", end="") # boş koltuk anlamına gelen 0 sayısı "-" sembolü şeklinde yazdırılmaktadır
            else:
                print("X", end="") # dolu koltuk anlamına gelen 1 sayısı "X" şeklinde yazdırılmaktadır
        print()
    ana_menu()


def salon_olustur():
    global kalan_koltuk
    kalan_koltuk = [100, 100, 100, 100] # her kategori için olmak üzere yüzer adet kalan koltuk sayısı belirlenmektedir
    # her rezervasyon işlemi sonrasında ilgili kategori için kalan koltuk sayısı azaltılmaktadır

    global ucret1,ucret2,ucret3,ucret4 # yeni etkinlik oluşturulduğunda var olan tüm rezervasyonlar sıfırlanmaktadır
    ucret1=0 # bu nedenle değişkenler başlangıç durumuna getirilmektedir
    ucret2=0
    ucret3=0
    ucret4=0

    global koltuk
    koltuk = [0] * 20
    for i in range(20):
        koltuk[i] = [0] * 20  # 20x20 çok boyutlu koltuk matrisi oluşturulmaktadır


# main kısmı
def main():
    dosya = open("indirim.txt", "r") # indirim.txt dosyası okuma modunda açılmaktadır

    list = []
    liste = []
    list = dosya.readlines()  # dosyadaki satırları alınmaktadır
    for i in range(len(list)):
        liste.append(list[i].strip()) 

    global ucretler
    ucretler = []  # her kategori için bilet ücretini tutacak ucretler[] listesi tanımlanmaktadır

    global indirim
    indirim = [0] * 12
    for i in range(12):
        indirim[i] = [0] * 3  # indirim 12x3 lük çok boyutlu matris olarak tanımlanmaktadır

    global maxBilet # tek seferde alınabilecek max bilet adedi tanımlanmaktadır

    for i in range(0, len(liste)):  # indirim.txt satırlarını okumaktadır
        if i == 0:  # ilk yani sıfırıncı satır, max bilet sayısını vermektedir
            carpan = 1
            maxBilet = 0
            for h in range(len(liste[i]) - 1, 1, -1):  # indirim.txt satırlarını tersten okumaktadır
                maxBilet += int(liste[i][h]) * carpan  # onlar basamağı olduğu için 10 ile çarpılmaktadır
                carpan *= 10
        if 1 <= i <= 4:  # 1 ila 4. satır arası, her kategori için bir bilet ücretini vermektedir
            carpan = 1
            sayi = 0
            for h in range(len(liste[i]) - 1, 1, -1):
                sayi += carpan * int(liste[i][h])
                carpan *= 10
            ucretler.append(sayi)
        if 5 <= i <= 16:  # 5 ila 16. satır arası, her kategori içim min-max bilet sayısına göre indirim oranlarını vermektedir
            indirim[i - 5][0] = int(liste[i][2]) * 10 + int(liste[i][3])
            if liste[i][5] == "M":  # i. satırın 5. harfi M sayısına denk geliyorsa
                indirim[i - 5][1] = 10  # M için, tek seferde alınabilecek max eleman olarak belirlenen 10 sayısı atanmaktadır
            else:
                indirim[i - 5][1] = int(liste[i][5]) * 10 + int(liste[i][6]) # indirim[][0], indirim için min bilet sayısını vermektedir
            try:
                indirim[i - 5][2] = int(liste[i][8]) * 10 + int(liste[i][9]) # indirim[][1], indirim için max bilet sayısını vermektedir
            except:
                indirim[i - 5][2] = int(liste[i][7]) * 10 + int(liste[i][8]) 
                # indirim[][2], bilet sayısına göre yapılacak indirim oranını vermektedir

    salon_olustur()
    ana_menu()

main()