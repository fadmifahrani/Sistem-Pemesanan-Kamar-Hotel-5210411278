class Petugas_Hotel:
    def __init__(self,id_petugas,nama,no_telepon,alamat):
        self.id_petugas = id_petugas
        self.nama = nama
        self.no   = no_telepon
        self.alamat= alamat

    def input(self):
        print("\n\n==========Info Pemesanan Kamar Hotel==========")
        print("\n-------------Petugas yang melayani--------------")
        print(f"ID Petugas    : {(self.id_petugas)}")
        print(f"Nama Petugas  : {(self.nama)}")
        print(f"Nomor Telepon : {(self.no)}")
        print(f"Alamat        : {(self.alamat)}")

class Tamu_Hotel:
    def __init__(self,nama,tempat_lahir,tanggal_lahir,jenis_kelamin,nomor_telpon,alamat):
        self.nama           = nama
        self.tempat_lahir   = tempat_lahir
        self.tanggal_lahir  = tanggal_lahir
        self.jenis_kelamin  = jenis_kelamin
        self.no             = nomor_telpon
        self.alamat         = alamat
        
    def input(self):
        print("\n-----------------Data Diri Tamu-----------------")
        print(f"Nama           :{self.nama}")
        print(f"Tempat Lahir   :{self.tempat_lahir}")
        print(f"Tanggal Lahir  :{self.tanggal_lahir}")
        print(f"Jenis Kelamin  :{self.jenis_kelamin}")
        print(f"Nomor Telepon  :{self.no}")
        print(f"Alamat         :{self.alamat}")

class Kamar:
    def __init__(self,tipe_kamar,tarif):
        self.tipe_kamar     = tipe_kamar
        self.tarif          = tarif
      
    def info(self):
        print("\n--------Pilihan Kamar---------")
        print("1. VIP")
        print("2. Standar")

class Vip(Kamar):
    def __init__(self,tipe_kamar,tarif,vasilitas):
        super(Vip,self).__init__(tipe_kamar,tarif)
        self.tipe_kamar   = tipe_kamar
        self.tarif        = tarif
        self.vasilitas    = vasilitas

    def info(self):
        print ("\n---------Tipe Kamar 1--------")
        print(f"Tipe Kamar       :{self.tipe_kamar}")
        print(f"Tarif            :{self.tarif}")
        print(f"Vasilitas        :{self.vasilitas}")


class Standar(Kamar):
    def __init__(self,tipe_kamar,tarif,vasilitas):
        super(Standar,self).__init__(tipe_kamar,tarif)
        self.tipe_kamar   = tipe_kamar
        self.tarif        = tarif
        self.vasilitas    = vasilitas

    def info(self):
        print ("\n--------Tipe Kamar 2---------")
        print(f"Tipe Kamar        :{self.tipe_kamar}")
        print(f"Tarif             :{self.tarif}")
        print(f"Vasilitas         :{self.vasilitas}")

class Booking:
    def __init__(self,nomor_kamar,lama_inap,tarif):
       self.nomor_kamar = nomor_kamar
       self.lama_inap = lama_inap
       self.tarif = tarif

    def pemesanan(self):
        print("")
        print(f"Nomor Kamar : {self.nomor_kamar}")
        print(f"Lama Inap   : {self.lama_inap}")
        print(f"Tarif       : {self.tarif}")

    def pembayaran(self):
        return print(f"Total Harga : {self.lama_inap * self.tarif}")
    

#INSTANSIASI OBJEK
data_petugas = Petugas_Hotel(
   int(input("ID Petugas      : ")),
   str(input("Nama Petugas    : ")),
   int(input("Nomor Telepon   : ")),
   str(input("Alamat         : ")))

data_tamu = Tamu_Hotel(
   str(input("Masukan Nama Tamu     : ")),
   str(input("Masukan Tempat Lahir  : ")),
   str(input("Masukan Tanggal Lahir : ")),
   str(input("Masukan Jenis Kelamin : ")),
   int(input("Masukan Nomor telepon : ")),
   str(input("Masukan Alamat        : ")))


kamar = Kamar("","")
vip = Vip(tipe_kamar="Vip",tarif="Rp 400.000,00 per malam",vasilitas = "AC, Televisi, Wifi, Kamar Mandi Dalam")
standar = Standar(tipe_kamar="Standar",tarif="Rp 150.000,00 per malam",vasilitas = "Kipas Angin, Televisi, Kamar Dandi Luar")
kamar.info()

opsi = input("Pilih Tipe kamar : ")
if opsi == '1':
    vip.info()
    booking = Booking(nomor_kamar=int(input("Nomor Kamar : ")),
                  lama_inap=int(input("Lama Inap : ")),
                  tarif=400000)
    data_petugas.input()
    data_tamu.input()
    print("\n------------Rincian Pemesanan Kamar------------")
    print("\nTipe kamar  : VIP")   
    booking.pemesanan()
    booking.pembayaran()
    

elif opsi == '2':
    standar.info()
    booking = Booking(nomor_kamar=int(input("Nomor Kamar : ")),
                  lama_inap=int(input("Lama Inap : ")),
                  tarif=150000)
    data_petugas.input()
    data_tamu.input()
    print("\n------------Rincian Pemesanan Kamar------------")
    print("\nTipe kamar : Standar")  
    booking.pemesanan()
    booking.pembayaran()

else:
    print("Inputan salah!")

print("\n===Terima Kasih Sudah Menggunakan Layanan Kami===")