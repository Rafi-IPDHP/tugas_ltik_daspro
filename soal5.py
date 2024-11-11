# Nama : Rafi Islami Pasha Dini Hari Putra
# NIM : 2404777
# Kelas : 1b

# Kakak Sepupu Client senang melakukan perhitungan
# matematika. Saat ini ia ingin menghitung jumlah bilangan yang lebih besar dari bilangan
# sebelumnya. Program akan terus berjalan hingga 3x angka yang diinputkan tidak ada yang
# lebih besar dari bilangan inputan sebelumnya. Bantulah sepupu dari client tersebut.

bil = int(input('Input bilangan: '))
membesar = []
kesempatan = 2

while True:
    new_bil = int(input('Input bilangan: '))
    if(kesempatan == 0):
        print(f'Hasil penjumlahan nilai yang membesar : {sum(membesar)}')
        break
    elif(new_bil < bil):
        kesempatan -= 1
    else:
        kesempatan = 2
        membesar.append(new_bil)

    bil = new_bil