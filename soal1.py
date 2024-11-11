# Nama : Rafi Islami Pasha Dini Hari Putra
# NIM : 2404777
# Kelas : 1b

# Client ingin membuat sebuah aplikasi yang disaat kita
# membuka aplikasi tersebut, kita diminta untuk login terlebih dahulu. Login disini
# diberikan kesempatan sebanyak 3 kali kesalahan untuk dapat masuk ke dalam aplikasi.
# Adapun username dan password yang diminta adalah

# Username: loginUTS
# Password: rpl2024

uname = 'loginUTS'
pw = 'uts2024'
kesempatan = 3

while kesempatan <= 3 and kesempatan > 0:
    kesempatan -= 1
    print('Silakan login\n')
    username = input('Username : ')
    password = input('Password : ')

    if(username == uname and password == pw):
        print('Selamat datang di aplikasi prodi RPL.')
    elif(kesempatan == 0):
        print('Anda tidak diperkenankan mengakses aplikasi ini.')
    else:
        print(f'Login Salah! Kesempatan Anda {kesempatan}x kali lagi.\n')