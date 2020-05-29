import os


# room_to_customer dosyasini yeniden yazma
def write_room_to_customer_file(room_to_customer):
    with open("room_to_customer_file.txt", "w") as room_to_customer_file:
        keys = list(room_to_customer.keys())
        for i in range(len(keys)):
            room_to_customer_file.write(
                str(keys[i]) + " " + str(room_to_customer[keys[i]]) + "\n")

# customer_data_file dosyasini yeniden yazma


def write_customer_data_file(customer_data):
    with open("customer_data_file.txt", "w") as customer_data_file:
        for i in range(len(customer_data)):
            for j in range(len(customer_data[i])):
                customer_data_file.write(customer_data[i][j] + " ")
            customer_data_file.write("\n")


# Dosyalari Okuma

def initialize_data():
    with open("customer_data_file.txt", "r") as customer_data_file:
        customer_data = [(line.strip()).split() for line in customer_data_file]

    with open("staff_data_file.txt", "r") as staff_data_file:
        staff_data = [(line.strip()).split() for line in staff_data_file]

    with open("room_data_file.txt", "r") as room_data_file:
        room_data = [(line.strip()).split() for line in room_data_file]

    with open("feedback_data_file.txt", "r") as feedback_data_file:
        feedback_data = [(line.strip()).split() for line in feedback_data_file]

    return customer_data, staff_data, room_data, feedback_data

# Oda Numarasina Gore Musteri Bilgilerini Gosterme


def get_customer_by_room_number(data, information_list, room_to_customer):

    while True:
        room_number = input(
            "Bilgilerini gormek istediginiz oda numarasini giriniz:")
        count = 0
        try:
            customer_id = room_to_customer[room_number]
        except KeyError:
            print("Arattiginiz oda bulunamadi.")
        else:
            for i in range(len(data)):
                if data[i][0] == customer_id:
                    for j in range(len(data[i])):
                        print("[{}] -> {}".format(information_list[j], data[i][j]))
                        count = 1

        if count == 0:
            print("Arattiginiz bilgi dogrultusunda birisi bulunamadi.")

        choose = int(input(
            "\n[1] -> Yeni Oda Arat \t[2] -> Menuye don\nYapmak istediginiz islemi seciniz:"))

        if choose == 1:
            print("Yeni Arama Islemi Baslatiliyor...")
            continue
        elif choose == 2:
            print("Ana menuye donuluyor...")
            break
        else:
            print("Hatali bir giris yaptiniz. Ana menuye donuluyor...")
            break

# Odaya Gore Musteri Dosyasini Okuma


def read_room_to_customer():
    with open("room_to_customer_file.txt", "r") as room_to_customer_file:
        lines = room_to_customer_file.read().splitlines()
        for line in lines:

            x = line.split(" ")
            room_to_customer[x[0]] = x[1]


# Oda Ucreti Hesaplama


def calculate_room_fee(room_types):
    while True:
        room_type = input(
            "1-Kucuk / 80 TL \t 2-Orta / 100 TL \t 3-Buyuk / 150 TL \t 4-Luks / 180 TL \nOda Türünü Giriniz:")
        day_to_stay = input("Kalınacak Gun Sayısını Giriniz:")
        print("{} Tipindeki Odada {} Gun Kalmanın Ücreti = {} TL" .format(room_types[int(
            room_type)-1][2], day_to_stay, int(room_types[int(room_type)-1][1])*int(day_to_stay)))

        choose = int(
            input("1-Ana Menuye Don \t 2-Tekrar Ucret Hesapla\nLutfen seciminizi yapiniz:"))
        if choose == 1:
            print("Ana menuye donuluyor...")
            break
        elif choose == 2:
            print("Tekrar arama isi baslatiliyor...")
            continue
        else:
            print("Hatali secim yaptiniz. Ana menuye donuluyor...")
            break

# Musteri Memnuniyeti Formlarini Listeleme


def list_feedback_forms(data, info):
    for i in range(len(info)):
        if i == 0:
            print("{}{}".format(info[i], " "*4), end="")
            continue
        print("{}{}".format(
            info[i], " "*(24-len(info[i]))), end="")
    print("\n")

    for i in range(len(data)):
        for j in range(len(data[i])):
            if j == 0:
                print("{}{}".format(data[i][j], " "*5), end="")
                continue
            print("{}{}  {}/5{}".format("|"*int(data[i][j]), "•"*(
                5-int(data[i][j])), data[i][j], " "*(15-len(data[i][j]))), end="")
        print("\n")
    print("\n\n")

# Musteri Memnuniyeti Orani


def feedback_rate(data, info):
    for i in range(len(info)):
        if i == 0:
            continue
        print("{}{}".format(
            info[i], " "*(25-len(info[i]))), end="")
    print("\n")
    total = 0
    customer_count = len(data)
    for i in range(len(data[0])):
        for j in range(len(data)):
            if i == 0:
                continue
            total += int(data[j][i])
        if i == 0:
            continue
        print("{:.2f}/100{}".format((100/(5*customer_count)) * total, " "*16), end="")
        total = 0
    print("\n\n")

# Musteri Memnuniyeti Formu Ekleme


def fill_feedback_form(data, info):
    temp_data = []
    temp_data.append(str(len(data)))
    for i in range(len(info)):
        if i == 0:
            continue
        temp_data.append(input(
            "{} için minimum 1 maksimum 5 olmak üzere bir sayi girin:".format(info[i])))
    data.append(temp_data)

    with open("feedback_data_file.txt", "w") as feedback_data_file:
        for i in range(len(data)):
            for j in range(len(data[i])):
                feedback_data_file.write(data[i][j] + " ")
            feedback_data_file.write("\n")

# Musteri Ekleme


def add_customer(data):
    temp_data = []
    temp_data.append(str(len(data)))
    temp_data.append(input("Musterinin TC Nosunu Giriniz:"))
    temp_data.append(input(
        "Not: Eger kisinin iki adi var ise '_' ile ayriniz ve Turkce karakter girmeyiniz.\nMusterinin Adini Giriniz:"))
    temp_data.append(
        input("Not: Turkce karakter girmeyiniz.\nMusterinin Soyadini Giriniz:"))
    age = input("Musterinin Yasini Giriniz:")
    temp_data.append(age)
    if int(age) >= 18:
        temp_data.append(
            input("Musterinin Medeni Durumunu(Evli-Bekar) Giriniz:"))
        temp_data.append(input("Musterinin Cocuk Sayisini Giriniz:"))
    else:
        temp_data.append("YOK")
        temp_data.append("YOK")
    room_number = input("Musteriyi eklemek isteginiz odayi giriniz:")
    temp_data.append(room_number)
    data.append(temp_data)
    write_customer_data_file(data)

    with open("room_to_customer_file.txt", "a") as room_to_customer_file:
        room_to_customer_file.write(
            "\n" + room_number + " " + temp_data[0])

    print("Musteri Basariyla Eklendi. Musteri Menusune Donuluyor...")

# Personel Ekleme


def add_staff(data):
    temp_data = []
    temp_data.append(str(len(data)))
    temp_data.append(input("Personelin TC Nosunu Giriniz:"))
    temp_data.append(input(
        "Not: Eger kisinin iki adi var ise '_' ile ayriniz ve Turkce karakter girmeyiniz.\nPersonelin Adini Giriniz:"))
    temp_data.append(
        input("Not: Turkce karakter girmeyiniz.\nPersonelin Soyadini Giriniz:"))
    temp_data.append(input("Personelin Yasini Giriniz:"))
    temp_data.append(input("Personelin Calisacagi Departmanin Adini Giriniz:"))
    data.append(temp_data)
    with open("staff_data_file.txt", "w") as staff_data_file:
        for i in range(len(data)):
            for j in range(len(data[i])):
                staff_data_file.write(data[i][j] + " ")
            staff_data_file.write("\n")
    print("Personel Basariyla Eklendi. Musteri Menusune Donuluyor...")

# Oda Ekleme


def add_room(data):
    temp_data = []
    temp_data.append(str(len(data)))
    temp_data.append(input("Oda türünü giriniz:"))
    temp_data.append(input("Oda fiyatini giriniz giriniz:"))
    data.append(temp_data)
    with open("room_data_file.txt", "w") as room_data_file:
        for i in range(len(data)):
            for j in range(len(data[i])):
                room_data_file.write(data[i][j] + " ")
            room_data_file.write("\n")
    print("Oda Basariyla Eklendi. Oda Menusune Donuluyor...")

# Arama Fonksiyonu +


def search_data(data, information_list):
    while True:
        # Aratilabilecek Bilgileri Gosterir
        for i in range(len(information_list)):
            print("[{}] - {}'a Gore Ara".format(i +
                                                1, information_list[i]), end="\t")

        search_type = int(input("\nArama Turunu Giriniz:"))-1
        search_keywords = input("{} Giriniz:".format(
            information_list[search_type]))
        # Arama Dongusu
        count = 0
        for i in range(len(data)):
            if data[i][search_type] == search_keywords:
                for j in range(len(data[i])):
                    print("[{}] -> {}".format(information_list[j], data[i][j]))
                count = 1

        if count == 0:
            print("Arattiginiz bilgi dogrultusunda birisi bulunamadi.")

        choose = int(input(
            "\n[1] -> Yeni Kisi Arat \t[2] -> Menuye don\nYapmak istediginiz islemi seciniz:"))

        if choose == 1:
            print("Yeni Arama Islemi Baslatiliyor...")
            continue
        elif choose == 2:
            print("Ana menuye donuluyor...")
            break
        else:
            print("Hatali bir giris yaptiniz. Ana menuye donuluyor...")
            break

# Listeleme Fonksiyonu +


def list_data(data, information_list):
    # Gosterilen Bilgileri Yazdirir
    for i in range(len(information_list)):
        if i == 0:
            print("{}{}".format(information_list[i], " "*4), end="")
            continue
        print("{}{}".format(
            information_list[i], " "*(15-len(information_list[i]))), end="")
    print("\n")

    # Verileri Yazdirir
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j == 0:
                print("{}{}".format(data[i][j], " "*5), end="")
                continue
            print("{}{}".format(data[i][j],
                                " "*(15-len(data[i][j]))), end="")
        print("\n")
    print("\n\n")

# Guncelleme Fonksiyonu +


def update_data(data, information_list, x):
    while True:
        list_data(data, information_list)
        control = 0
        for i in range(len(information_list)):  # Guncellenebilecek Bilgileri Gosterir
            print("[{}] - {}".format(i+1, information_list[i]), end="\t")
        id_choose = int(
            input("\nDegistirmek istediginiz ID'yi giriniz:"))
        for i in range(len(data)):
            if int(data[i][0]) == int(id_choose):
                choose = int(
                    input("\nDegistirmek istediginiz bilgiyi seciniz:"))
                if choose == 1:  # ID ve Oda Numarasi Degistirilemez Bilgi Olarak Ayarlanmistir
                    print("ID Degistirilemez.")
                    break
                if x == 1 and choose == 8:
                    print("Oda Numarasi Degistirilemez.")
                    break
                updated_info = input("\nBilgiyi giriniz:")
                data[id_choose][choose-1] = updated_info
                control = 1

        # Dosyayi yeniden yazar
        if control == 1:
            if x == 1:
                with open("customer_data_file.txt", "w") as customer_data_file:
                    for i in range(len(data)):
                        for j in range(len(data[i])):
                            customer_data_file.write(data[i][j] + " ")
                        customer_data_file.write("\n")

            elif x == 2:
                with open("staff_data_file.txt", "w") as staff_data_file:
                    for i in range(len(data)):
                        for j in range(len(data[i])):
                            staff_data_file.write(data[i][j] + " ")
                        staff_data_file.write("\n")

            elif x == 3:
                with open("room_data_file.txt", "w") as room_data_file:
                    for i in range(len(data)):
                        for j in range(len(data[i])):
                            room_data_file.write(data[i][j] + " ")
                        room_data_file.write("\n")

            print("Bilgi Basariyla Guncellendi. Menuye Donuluyor...")
            break
        else:
            print("Arattiginiz ID Bulunamadi. Lutfen tekrar deneyiniz...")

# Silme Fonksiyonları +

# ID Kontrolu Yapar


def find_id(data, temp_id):
    for i in range(len(data)):
        if data[i][0] == temp_id:
            return i
    return None

# Personelin Calistigi Bolumu "BOS" Yapar


def remove_staffs_department_information(data, temp_id):
    staff_id = find_id(data, temp_id)
    if staff_id == None:
        return False
    else:
        data[staff_id][5] = "BOS"
        return True


def remove_staff(data, information_list):
    while True:
        list_data(data, information_list)
        temp_id = input("Silmek istediginiz ID'yi giriniz:")
        is_staff_exist = remove_staffs_department_information(data, temp_id)

        # Dosyayi yeniden yazar
        if is_staff_exist:
            with open("staff_data_file.txt", "w") as staff_data_file:
                for i in range(len(data)):
                    for j in range(len(data[i])):
                        staff_data_file.write(data[i][j] + " ")
                    staff_data_file.write("\n")
            print("Bilgi basariyla Silindi. Menuye Donuluyor...")
            break
        else:
            print("Arattiginiz ID Bulunamadi. Lutfen tekrar deneyiniz...")
            continue


def remove_customers_room_information(data, temp_id):
    customer_id = find_id(data, temp_id)
    if customer_id == None:
        return False
    else:
        data[customer_id][7] = "-"
        return True


def find_customers_room(customer_id, room_to_customer):
    keys = list(room_to_customer.keys())
    for i in range(len(keys)):
        if int(room_to_customer[keys[i]]) == int(customer_id):
            return keys[i]
    return None


def remove_customer(data, information_list, room_to_customer):
    while True:
        list_data(data, information_list)
        temp_id = input("Silmek istediginiz ID'yi giriniz:")
        is_customer_exist = remove_customers_room_information(data, temp_id)

        if is_customer_exist:

            # Eger Oda Bulunursa Odadaki Musteri Bilgilerini Siler
            room_id = find_customers_room(temp_id, room_to_customer)
            room_to_customer.pop(room_id)

           # Dosyalari yeniden yazar
            write_customer_data_file(data)
            write_room_to_customer_file(room_to_customer)

            print("Bilgi basariyla Silindi. Menuye Donuluyor...")
            break
        else:
            print("Arattiginiz ID Bulunamadi. Lutfen tekrar deneyiniz...")
            continue


# Menüler


def get_customer_menu():
    os.system('cls')
    while True:
        # Isim ve Ust Cizgi
        print("\t\t\t\t\t\t    Musteri Bolumu" +
              "\n\t\t\t\t\t=======================================")

        # Menu Maddeleri
        for i in range(len(customer_menu)):
            print("\t\t\t\t\t| [{}] {}{}|".format(
                i+1, customer_menu[i], " "*(32-len(customer_menu[i]))))
            quit_number = i+2

        # Cikis
        print("\t\t\t\t\t| [{}] Ana Menuye Don{}|".format(
            quit_number, " "*(18)))

        # Alt Cizgi
        print("\t\t\t\t\t=======================================")

        # Secim Bolumu
        choose = int(input("\t\t\t\t\tSecim Yapiniz:"))

        if choose == 1:  # Musteri Ekleme
            os.system('cls')
            add_customer(customer_data)
        elif choose == 2:  # Musteri Bilgisi Guncelleme
            os.system('cls')
            update_data(customer_data,
                        customer_information_list, 1)
        elif choose == 3:  # Musteri Aratma
            os.system('cls')
            search_data(customer_data, customer_information_list)
        elif choose == 4:  # Musteri Listeleme
            os.system('cls')
            while True:
                list_data(customer_data, customer_information_list)
                choose_in_lists = input(
                    "1- Ana Menuye Don 2- Tekrar Listele.\nNe yapmak istediginizi seciniz:")
                if int(choose_in_lists) == 1:
                    break
                elif int(choose_in_lists) == 2:
                    continue
                else:
                    print(
                        "Hatali secim yaptiniz. Ana menuye donuluyor...")
                    break

        elif choose == 5:  # Musteri Silme
            os.system('cls')
            remove_customer(
                customer_data, customer_information_list, room_to_customer)
        elif choose == 6:  # Oda Ucreti Hesapla
            calculate_room_fee(room_types)
        elif choose == 7:
            print("\t\t\t\t\tAna menuye donuluyor...")
            os.system('cls')
            break
        else:
            print(
                "\t\t\t\t\tHatali bir secim yaptiniz, secim ekranina yonlendiriliyorsunuz...")
            os.system('cls')
            continue


def get_staff_menu():
    os.system('cls')
    while True:
        # Isim ve Ust Cizgi
        print("\t\t\t\t\t\t    Personel Bolumu" +
              "\n\t\t\t\t\t=======================================")

        # Menu Maddeleri
        for i in range(len(staff_menu)):
            print("\t\t\t\t\t| [{}] {}{}|".format(
                i+1, staff_menu[i], " "*(32-len(staff_menu[i]))))
            quit_number = i+2

        # Cikis
        print("\t\t\t\t\t| [{}] Ana Menuye Don{}|".format(
            quit_number, " "*(18)))

        # Alt Cizgi
        print("\t\t\t\t\t=======================================")

        # Secim Bolumu
        choose = int(input("\t\t\t\t\tSecim Yapiniz:"))

        if choose == 1:  # Personel Listeleme
            os.system('cls')
            while True:
                list_data(staff_data, staff_information_list)
                choose_in_lists = input(
                    "1- Ana Menuye Don 2- Tekrar Listele.\nNe yapmak istediginizi seciniz:")
                if int(choose_in_lists) == 1:
                    break
                elif int(choose_in_lists) == 2:
                    continue
                else:
                    print(
                        "Hatali secim yaptiniz. Ana menuye donuluyor...")
                    break

        elif choose == 2:  # Yeni Personel Ekleme
            os.system('cls')
            add_staff(staff_data)

        elif choose == 3:  # Personel Bilgilerini Guncelleme
            os.system('cls')
            update_data(staff_data, staff_information_list, 2)

        elif choose == 4:  # Personel Silme
            os.system('cls')
            remove_staff(staff_data, staff_information_list)

        elif choose == 5:  # Personel Arama
            os.system('cls')
            search_data(staff_data, staff_information_list)

        elif choose == 6:
            print("\t\t\t\t\tAna menuye donuluyor...")
            os.system('cls')
            break

        else:
            print(
                "\t\t\t\t\tHatali bir secim yaptiniz, secim ekranina yonlendiriliyorsunuz...")
            os.system('cls')
            continue


def get_room_menu():
    os.system('cls')
    while True:
        # Isim ve Ust Cizgi
        print("\t\t\t\t\t\t       Oda Menusu" +
              "\n\t\t\t\t\t=======================================")

        # Menu Maddeleri
        for i in range(len(room_menu)):
            print("\t\t\t\t\t| [{}] {}{}|".format(
                i+1, room_menu[i], " "*(32-len(room_menu[i]))))
            quit_number = i+2

        # Cikis
        print("\t\t\t\t\t| [{}] Ana Menuye Don{}|".format(
            quit_number, " "*(18)))

        # Alt Cizgi
        print("\t\t\t\t\t=======================================")

        # Secim Bolumu
        choose = int(input("\t\t\t\t\tSecim Yapiniz:"))
        if choose == 1:  # Odalari Listele
            os.system('cls')
            while True:
                list_data(room_data, room_information_list)
                choose_in_lists = input(
                    "1- Ana Menuye Don 2- Tekrar Listele.\nNe yapmak istediginizi seciniz:")
                if int(choose_in_lists) == 1:
                    break
                elif int(choose_in_lists) == 2:
                    continue
                else:
                    print(
                        "Hatali secim yaptiniz. Ana menuye donuluyor...")
                    break
        elif choose == 2:  # Yeni Oda Ekle
            os.system('cls')
            add_room(room_data)
        elif choose == 3:  # Oda Bilgisi Guncelle
            os.system('cls')
            update_data(room_data, room_information_list, 3)
        elif choose == 4:  # Odadaki Musteri Bilgilerini Goruntule
            os.system('cls')
            get_customer_by_room_number(
                customer_data, customer_information_list, room_to_customer)
        elif choose == 5:
            print("\t\t\t\t\tAna menuye donuluyor...")
            os.system('cls')
            break


def get_feedback_menu():
    os.system('cls')
    while True:
        # Isim ve Ust Cizgi
        print("\t\t\t\t\t\t  Musteri Memnuniyeti" +
              "\n\t\t\t\t\t=======================================")

        # Menu Maddeleri
        for i in range(len(feedback_menu)):
            print("\t\t\t\t\t| [{}] {}{}|".format(
                i+1, feedback_menu[i], " "*(32-len(feedback_menu[i]))))
            quit_number = i+2

        # Cikis
        print("\t\t\t\t\t| [{}] Ana Menuye Don{}|".format(
            quit_number, " "*(18)))

        # Alt Cizgi
        print("\t\t\t\t\t=======================================")

        # Secim Bolumu
        choose = int(input("\t\t\t\t\tSecim Yapiniz:"))
        if choose == 1:  # Geri Bildirim Formu Doldurma
            os.system('cls')
            fill_feedback_form(
                feedback_data, feedback_information_list)
        elif choose == 2:  # Geri Bildirim Formlarini Listeleme
            os.system('cls')
            list_feedback_forms(
                feedback_data, feedback_information_list)
        elif choose == 3:  # Memnuniyet Oranı
            os.system('cls')
            feedback_rate(feedback_data, feedback_information_list)
        elif choose == 4:
            print("\t\t\t\t\tAna menuye donuluyor...")
            os.system('cls')
            break


def get_menus():
    while True:
        # Isim ve Ust Cizgi
        print("\t\t\t\t\t\t    OTEL OTOMASYONU" +
              "\n\t\t\t\t\t=======================================")

        # Menu Maddeleri
        for i in range(len(hotel_menu)):
            print("\t\t\t\t\t| [{}] {}{}|".format(
                i+1, hotel_menu[i][1], " "*(32-len(hotel_menu[i][1]))))
            quit_number = i+2

        # Cikis
        print("\t\t\t\t\t| [{}] Cikis{}|".format(quit_number, " "*(27)))

        # Alt Cizgi
        print("\t\t\t\t\t=======================================")

        # Secim Bolumu
        choose = int(input("\t\t\t\t\tSecim Yapiniz:"))

        # Musteri Menusu
        if choose == 1:
            get_customer_menu()
        # Personel Menusu
        elif choose == 2:
            get_staff_menu()
        # Oda Menusu
        elif choose == 3:
            get_room_menu()
        # Musteri Memnuniyeti Menusu
        elif choose == 4:
            get_feedback_menu()
        elif choose == 5:
            print("\t\t\t\t\tProgramdan cikiliyor...")
            break
        else:
            print(
                "\t\t\t\t\tHatali bir secim yaptiniz, secim ekranina yonlendiriliyorsunuz...")
            os.system('cls')
            continue


def main():
    read_room_to_customer()
    get_menus()


# Menü Verileri
customer_menu = ["Odaya Musteri Ekle", "Musteri Bilgilerini Guncelle", "Musteri Ara",
                 "Musterileri Listele", "Musteriyi Sil", "Oda Ücreti Hesapla"]
room_menu = ["Odalari Listele", "Oda Ekle",
             "Oda Bilgilerini Guncelle", "Odadaki Musteri Bilgileri"]
staff_menu = ["Personelleri Listele", "Personel Ekle",
              "Personel Bilgisi Guncelle", "Personel Sil", "Personel Ara"]
feedback_menu = ["Geri Bildirim Formu Doldur", "Geri Bildirim Formlarini Listele",
                 "Otel Memnuniyet Oranlarini Gor"]
hotel_menu = [[customer_menu, "Musteri Menusu"], [staff_menu, "Personel Menusu"], [
    room_menu, "Oda Menusu"], [feedback_menu, "Musteri Memnuniyeti Menusu"]]

# Bilgiler
customer_information_list = ["ID", "TC Kimlik No", "Ad",
                             "Soyad", "Yas", "Medeni Durum", "Cocuk Sayisi", "Oda Numarası"]
staff_information_list = ["ID", "TC Kimlik No", "Ad",
                          "Soyad", "Yas", "Departman"]
room_information_list = ["ID", "Oda Türü", "Fiyat"]
feedback_information_list = ["ID", "Oda Puanlamasi",
                             "Hizmet Puanlamasi", "Temizlik Puanlamasi", "Personel Puanlamasi"]

# Veriler
customer_data, staff_data, room_data, feedback_data = initialize_data()
room_to_customer = {}
room_types = [[1, 80, "KUCUK"], [2, 100, "ORTA"],
              [3, 150, "BUYUK"], [4, 180, "LUKS"]]


main()
