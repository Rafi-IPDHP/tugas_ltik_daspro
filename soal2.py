# Nama : Rafi Islami Pasha Dini Hari Putra
# NIM : 2404777
# Kelas : 1b

# Client menginginkan sebuah program yang dapat membaca
# sekumpulan bilangan bulat positif. Selain itu, dia ingin program tersebut juga berhenti
# membaca ketika user menginputkan bilangan negatif. Jika user menginputkan bilangan
# negatif, maka berikutnya program tersebut mencetak masing-masing jumlah bilangan
# genap dan bilangan ganjil yang telah diinputkan, dengan catatan nilai 0 adalah bilangan
# genap.

genap = []
ganjil = []

while True:
    bil = int(input('Masukkan bilangan : '))

    if(bil < 0):
        break

    if(bil % 2 == 0):
        genap.append(bil)
    else:
        ganjil.append(bil)

print(f'Jumlah bilangan genap adalah {sum(genap)}')
print(f'Jumlah bilangan ganjil adalah {sum(ganjil)}')