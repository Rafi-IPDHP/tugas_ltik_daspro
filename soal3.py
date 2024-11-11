# Nama : Rafi Islami Pasha Dini Hari Putra
# NIM : 2404777
# Kelas : 1b

# Adik bungsu dari client tersebut yang memiliki kemauan
# belajar yang terbilang unik. Adiknya hanya ingin belajar dengan menggunakan sebuah
# lagu yang dapat dinyanyikan. Client pun meminta untuk membuat sebuah program untuk
# bernyanyi “Bebek Kecil” dari jumlah yang di inputkan oleh user sebanyak N. Misalkan,
# jika user memasukkan nilai N = 5 maka program akan berjalan sebagai berikut:

n = int(input('Berapa kali lagu akan diputar: '))

for i in range(n):
    if(n == 1):
        print(f'{n} bebek kecil berenang\nMenyusuri sungai yang deras\nInduknya mencari kwek kwek kwek\nDan semua bebek kecil pulang, aha!')
    else:
        print(f'{n} bebek kecil berenang\nMenyusuri sungai yang deras\nInduknya mencari kwek kwek kwek\nHanya {n-1} ekor yang pulang')

    n -= 1