# variable dan tipe data
dafin_mhs ="dafin" 
kelas = "C1"

nilaia_a = int(input('MASUKKAN NILAI BAHASA INDONESIA: '))
nilai_b = int(input('MASUKKAN NILAI ALGORITMA: '))
nilai_c = int(input('MASUKKAN NILAI PKN: '))
nilai_d = int(input('MASUKKAN NILAI BASIS DATA: '))
nilai_e = int(input('MASUKKAN NILAI AGAMA: '))
nilai_f = int(input('MASUKKAN NILAI INFORMATIKA: '))
nilai_g = int(input('MASUKKAN NILAI BAHASA INGGRIS: '))
rata_rata = (nilaia_a + nilai_b + nilai_c + nilai_d + nilai_e + nilai_f + nilai_g) / 7       

if rata_rata >= 90 and rata_rata <= 100:
    print("Nilai : A" )
elif rata_rata >= 80 and rata_rata < 90:
    print("Nilai : B" )
elif rata_rata >= 70 and rata_rata < 80: 
    print("Nilai : C" ) 
    print("Nilai : C" )
elif rata_rata >= 60 and rata_rata < 70:
    print("Nilai : D" )
else:
    print("Nilai : E" )

# rata_rata = (nalgoritma + nagama + nbasisdata) / 3
# print(rata_rata)
nilai = int(input('MASUKKAN NILAI: '))

# penetuan lulus atau tidak
if rata_rata >=80 and rata_rata <=100:
    #kondisi jika terpenuhi
    #maka
    print("Nilai : A" )
elif rata_rata >=70 and rata_rata <=80:
    print("Nilai : B" )
elif rata_rata >=50 and rata_rata <=70:
    print("Nilai : C" )
elif rata_rata >=20 and rata_rata <=50:
    print("Nilai : D" )
elif rata_rata >=0 and rata_rata <= 20:
    print("Nilai : E" )
else:   
    # cukup menampilkan hasil
    # maka
    print("nilai lebih dari 100 atau dibawah 50")