# Nama : Rafi Islami Pasha Dini Hari Putra
# NIM : 2404777
# Kelas : 1b

# Saat ada mahasiswa yang memiliki 3-digit NIM terakhirnya ganjil, maka dia akan masuk
# ke kelas ganjil, begitupun mahasiswa yang 3-digit NIM terakhirnya adalah genap.

nim = int(input('Input 3 digit NIM terakhir: '))

if(nim >= 1 and nim <= 50):
    if(nim % 2 == 0):
        print('Silakan masuk ke kelas K2')
    else:
        print('Silakan masuk ke kelas K1')
elif(nim >= 51 and nim <= 100):
    if(nim % 2 == 0):
        print('Silakan masuk ke kelas K4')
    else:
        print('Silakan masuk ke kelas K3')
elif(nim >= 101 and nim <= 150):
    if(nim % 2 == 0):
        print('Silakan masuk ke kelas K6')
    else:
        print('Silakan masuk ke kelas K5')
elif(nim >= 151):
    if(nim % 2 == 0):
        print('Silakan masuk ke kelas K8')
    else:
        print('Silakan masuk ke kelas K7')
else:
    print('NIM tidak boleh 0 atau kurang dari 0')

