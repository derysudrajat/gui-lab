## Latihan 1
print("===================== Latihan 1 =====================")
myFile = open("prodi.txt")  # mendapatkan data dari file
content = myFile.read()  # membaca data
myFile.close()  # menutup data file
print(content)  # mencetak data yang telah di baca
print(type(myFile))  # mengeecek type dari file

print("===================== Splitline =====================")
# kalimat yang dipissahkan oleh \n atau baris baru
aku = "aku\nadalah\nanak\ngembala"
# mencetak kalimat dengan menjadikan sebagai array dengan memisahkan \n
print(aku.splitlines())
# melakukan perulangan dengan memisahkan kalimat dengan \n
for x in aku.splitlines():
    # hasil x yang dimana adalah nilai array dari kalimat `aku` yang sudah dipisahkan simbol \n nya
    print(x)

print("===================== Latihan 2 =====================")
## Latihan 2
blackpink = ["Lisa", "Jennie", "Rose", "Ji-Soo"]  # array berupa nama personel black pink
for x in blackpink:  # melakukan perulangan sebanyak jumlah array dari array `blackpink`
    print(x)  # cetak nilai x adalah perulangan dari array `blackpink`

print("===================== Tambah 5 =====================")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # array berisikan nilai dari 1-10
for i in a:  # perulangan sebanyak array a
    b = i + 10  # `b` adalah variable baru dari nilai perulangan + 10
    print(b)  # cetak nilai b

print("===================== Latihan 3 =====================")
## Latihan 3
"""
    program untuk memilah dan mencetak nilai array 
    yang dimana nilainya lebih dari 5 dengan perulangan
"""
myList = [3, 4, 6, 11, 2, 17, 90]
for b in myList:
    if b > 5: print(b)  # cetak nilai jika lebih dari 5

print("===================== Latihan 4 =====================")
## Latihan 4
"""
    mencetak panjang sebuah kata dari array yang ada di file
    :param mfruit.txt
"""
buatGw = open("mfruit.txt")  # mendapatkan file dari `mfruit.txt`
contentBuah = buatGw.read()  # membaca data dari file
buatGw.close()  # menutup file

# mencetak nilai pada file dengen memisahkan barisnya
for mm in contentBuah.splitlines():
    print(len(mm))  # mencetak panjang dari kata

print("===================== Fungsi Convert =====================")
temper = [10, -20, 100]  # array suhu celcius

"""
    fungsi `cel_to_fahr` mengubah suhu celcius
    ke suhu fahrenheit dengan parameter inputan
    :param celcius
"""


def cel_to_fahr(celcius):
    fahrenheit = celcius * 9 / 5 + 32
    return fahrenheit


# perulangan sebanyak array `temper`
for t in temper:
    # cetak nilai temper yang akan di konvert ke fahrenfeit
    print(cel_to_fahr(t))

"""
    program dibawah ini akan memproses,
    menambahkan data pada file `pegawai.txt` 
"""
theFile = open("pegawai.txt", "a")
# menuliskan data baru pada varibale theFile
theFile.write("Bambs")
theFile.write("\nLisa")
theFile.write("\nPenaldo")
theFile.write("\nKubo")
theFile.close()  # menutup file
# membaca data yang ada di file theFile
theFile2 = open("pegawai.txt")
mContent = theFile2.read()
theFile2.close()
# mencetak content file yang sudah dibaca
print(mContent)
