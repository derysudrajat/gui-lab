## Latihan 1
print("===================== Latihan 1 =====================")
myFile = open("prodi.txt")
content = myFile.read()
myFile.close()
print(content)
print(type(myFile))
print("===================== Splitline =====================")
aku = "aku\nadalah\nanak\ngembala"
print(aku.splitlines())
for x in aku.splitlines():
    print(x)
print("===================== Latihan 2 =====================")
## Latihan 2
blackpink = ["Lisa", "Jennie", "Rose", "Ji-Soo"]
for x in blackpink:
    print(x)
print("===================== Tambah 5 =====================")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    b = i + 10
    print(b)
print("===================== Latihan 3 =====================")
## Latihan 3
myList = [3, 4, 6, 11, 2, 17, 90]
for b in myList:
    if b > 5: print(b)
print("===================== Latihan 4 =====================")
## Latihan 4
buatGw = open("mfruit.txt")
contentBuah = buatGw.read()
buatGw.close()
for mm in contentBuah.splitlines():
    print(len(mm))

print("===================== Fungsi Convert =====================")
temper = [10, -20, 100]


def cel_to_fahr(celcius):
    fahrenheit = celcius * 9 / 5 + 32
    return fahrenheit


for t in temper:
    print(cel_to_fahr(t))
theFile = open("pegawai.txt","a")
theFile.write("Bambs")
theFile.write("\nLisa")
theFile.write("\nPenaldo")
theFile.write("\nKebo")
theFile.close()
