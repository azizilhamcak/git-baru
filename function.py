def sum (y):
    out = y + 12
    return out
i = sum (10)
print(i)

def kenalan(nama, umur):
    out = f"Nama saya {nama}, umur saya {umur} tahun"
    return out
i = kenalan("Jojo", 23)
print(i)

def pangkat(x, y):
    out = x**y
    return out
i = pangkat(2, 3)
print(i)

def combine(list1=list, list2 = list):
    return(list2.extend(list1))

list1 = [1, 2, 3, 4, 5, 6]       
list2 = [7, 8, 9, 10, 11, 12]
combine(list1, list2)
print(list2)