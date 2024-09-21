#nama = input('Masukkan nama: ')
#umur = int (input('masukkan umur: '))
#print(f'hello {nama}, {umur}tahun')
#print(type(umur))

data = ''
databaru = []

data = input("Masukkan Nilai Siswa: ")
while data.lower() != 'simpan':
    if data:
        databaru.append(data)
        data = input("Masukkan Nilai Siswa: ")
        
def tampil ():
     print("\nNILAI UJIAN KELAS 10")
     for i in databaru:
        print (i)
    
tampil()