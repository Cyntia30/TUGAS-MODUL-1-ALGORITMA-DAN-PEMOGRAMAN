# percabangan
# menggunakan statment IF

# struktur
"""
    1. if-nya
    2. Ada kondisi (bernilai TRUE/FALS)
    3. Ada Aksi -> proses lanjutan
"""

nama = input("masukkan nama anda = ")

# If statement dalam bentuk inline (satu baris)
# if nama == "cyntia" : print(f"selamat datang {nama}")
# print("Terima Kasih")

# if statement dalam bentuk indentasi
#if nama == 'cyntia' :
 #    print(f'Selamat Datang {nama}')
#print("Terima Kasih")

# IF-ELSE Statement
if nama == 'cyntia':
    # aksi 1
    print(f'Selamat Datang {nama}')
else:
    # aksi 2
    print(f'kamu {nama}, bukan cyntia')
print('terima kasih')
