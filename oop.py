class Motor:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
    
    def servis(self):
        print(f"Motor dengan merk {self.merk} {self.warna} {self.tahun} sudah waktunya ganti oli ")
    
    def pajak(self):
        print(f"Motor dengan merk {self.merk} {self.warna} {self.tahun} sudah waktunya bayar pajak ")
    
motor1 = Motor("honda", "win", 2010)
motor2 = Motor("yamaha", "mio", 2015)
motor3 = Motor("suzuki", "x-ride", 2018)
motor1.pajak()
motor2.servis()
motor3.servis() 