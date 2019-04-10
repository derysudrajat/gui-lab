'''
def haha(angka):
    for x in angka:
        for a in x:
            print("*")
            x -=1
'''


def haha(angka):
    for x in range(angka):
        b = '*' * (angka-x) + '\n'
        print(b)

haha(5)
'''
import csv

with open('haha.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

csvFile.close()
'''

import pandas as pd
data = pd.read_csv("haha.csv")
print(data.head())
print("====================")
data_array = data.values
ukuran = data_array.shape
kolom = ukuran[1]
row = ukuran[0]

row_train = 8*(row//10)
x_train = data_array[:row_train, 0:2]
y_train = data_array[:row_train, 2]

x_test = data_array[row_train:, 0:2]
y_test = data_array[row_train:, 2]

print(x_train)

