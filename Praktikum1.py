###
# Dictionery
# /
print("============== Dictionary Section ================")
pins = {"Bejo": 1101, "Maman": 1234, "Otong": 3434}

print(pins["Bejo"])
print(type(pins["Maman"]))
print(pins.keys())
print(pins.values())

# add Paijo to Pins Dictionary
pins["Paijo"] = 3333
print(pins)

# delete Paijo from pins
pins.pop("Paijo")
print(pins)

# add Elok to Pins with String value
pins["Elok"] = "AB123"
print(pins)

###
# User Input Pyton
print()
print("============== User Input Section ================")
masukan = input("Please Input your name: ")  # input with string result
bilangan = int(input("Input Integer: "))  # input with int result

# result for masukan and bilangan
print(masukan)
print(bilangan ** 2)

pecahan = float(input("Masukan Bilangan Pecahan: "))  # input with float result
print("Hasil: ", pecahan / 2)  # result for pecahan

###
# Conditional
print()
print("============== Conditional Section ================")
print(pins.values())

# Identify did kode1 involve in pins dictionary
kode1 = 1101
isKode1 = kode1 in pins.values()
print(isKode1)

# conditional if - else
# less than
if 1 < 5:
    print("Yes")
else:
    print("No")

# if equal
if 1 == 5:
    print("Sama")
else:
    print("Beda")

###
# Multiple Condition
print()
print("============== Multiple Condition Section ================")
# check value of userInput and identify which one equal with the condition
userInput = float(input("Masukan Angka: "))
if userInput > 100:
    print(userInput, "Lebih besar dari 100")
elif userInput.__eq__(100):
    print(userInput, "Sama dengan 100")
else:
    print(userInput, "lebih kecil dari 100")

###
# Function
print()
print("============== Function Section ================")


# function printing will print"Hai \nBejo"
def printing():
    print("Hai \nBejo")


### function luasPersegi will calculate the params by itself
#  and put the result in luas var and will return the value
def luasPersegi(sisi):
    luas = sisi * sisi
    return luas

### function luasSegitiga will calculate the area of triangle
# with param alas and tinggi, alas will multipy by tinggi and divide by 2
# the result will put with luas var
def luasSegitiga(alas, tinggi):
    luas = float((alas * tinggi) / 2)
    print("Luas Segitiga :", luas)

### will calculate your age with param tahun which now year min by tahun param
# the result will put on mUmur var
def hitungUmur(tahun):
    mUmur = 2019-tahun
    print("Umur kamu: ", mUmur)


### this several way to call function
printing()
print(luasPersegi(2))
luasSegitiga(10, 5)
hitungUmur(1999)

