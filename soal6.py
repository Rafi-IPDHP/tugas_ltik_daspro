# Nama : Rafi Islami Pasha Dini Hari Putra
# NIM : 2404777
# Kelas : 1b

# Salah satu adik client diberikan sebuah list yang memiliki
# jumlah item sebanyak N bilangan. Bantulah adik client ini untuk menentukan jumlah
# bilangan prima pada setiap item list yang diinputkan. Dimana nilai dari setiap item pada
# list diisikan oleh user.

prima = []
n = int(input('Masukkan nilai N = '))

for i in range(n):
    bil = int(input(f'Masukkan bilangan ke-{i + 1} = '))

    prima_checker = False

    for x in range(2, bil):
        if(bil % x == 0):
            prima_checker = False
            break
    else:
        prima_checker = True
        
    if(prima_checker == True):
        prima.append(bil)
    else:
        prima_checker = False

print(f'Jumlah bilangan prima adalah {sum(prima)}')
