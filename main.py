input_data = []

def databis ():
    print('PROGRAM INPUT DATA, KETIK simpan UNTUK MENYIMPAN DATA')
    data = input('Masukkan data:  ')
    while data.lower() != 'simpan':
        input_data.append(data)
        data = input('Masukkan data:  ')
        
def tampil ():
    print('\nData yang di input adalah:')
    for item in input_data:
        print(item)
        
databis()
tampil()
        