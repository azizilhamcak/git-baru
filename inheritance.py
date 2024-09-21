class Motor:
    def __init__(self, merk, tipe, warna, tahun):
        self.merk = merk
        self.tipe = tipe
        self.warna = warna
        self.tahun = tahun

class service(Motor):
    def __init__(self, merk, tipe, warna, tahun, riwayat, pajak):
        super().__init__(merk, tipe, warna, tahun)
        self.riwayat = riwayat
        self.pajak = pajak
    
    def datamotor (self):
        print(f"Data motor anda dengan merk {self.merk}, tipe {self.tipe}, tahun pembuatan {self.tahun}, ganti oli terakhir {self.riwayat}km, status pajak {self.pajak} ")

motor1 = service ("honda", "win", "hitam", 2000, 53000, True)
motor2 = service ("yamaha", "mio", "biru", 2015, 10000, False)
motor1.datamotor()
motor2.datamotor()