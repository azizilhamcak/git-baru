ktp = {"nik": 123456789, "Nama": "Kaka Komala", "Tahun Lahir": 2005,
       "Hobi" : ["Membaca", "Sepeda"]}




agama = ktp.get("agama", "Islam")
print(agama)

ktp["nik"] = 67890
print(ktp)

ktp["Nilai UAS"] = [100, 90]
print(ktp)

ktp.update({"Rangking" : [10]})
print(ktp)

ktp.pop("nik")
print(ktp)

del ktp["Nama"]
print(ktp) 

ktp = {"nik": 123456789, "Nama": "Kaka Komala", "Tahun Lahir": 2005,
       "Hobi" : ["Membaca", "Sepeda"]}
x = ktp.popitem()
print(x)
print(x[1])


