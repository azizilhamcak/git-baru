class Motor:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
    
    def servis(self):
        print(f"Motor dengan merk {self.merk} {self.warna} {self.tahun} sudah waktunya ganti oli ")
class service:
    def __init__(self, riwayat, pajak):
        self.riwayat = riwayat
        self.pajak = pajak
    def datamotor (self):
        print(f"Data motor anda ganti oli terakhir {self.riwayat}km, status pajak {self.pajak} ")

class databengkel (Motor, service):
    def __init__(self, merk, warna, tahun, riwayat, pajak):
        Motor.__init__(self, merk, warna, tahun)
        service.__init__(self, riwayat, pajak)
    def servis(self):
        print(f"Motor dengan merk {self.merk} {self.warna}, tahun pembuatan {self.tahun} , ganti oli terakhir {self.riwayat}km, status pajak {self.pajak} ")
    
datamotor = databengkel("honda", "win", 2010, 53000, True)
datamotor.servis()