import csv

list = []
k = 0
count = 0
check = []
max_dow = 0
popularity = []
publisher = []

with open('books-en.csv', encoding = 'latin-1') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        list.append(row['Book-Title'])
for i in list:
    if len(i) > 30:
        count += 1
print('Количество строк у которых название больше 30: ', count)
author = input('Введите фамилию: ')
with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        if row[3] == author and (int(row[6]) == 2014 or int(row[6]) == 2016 or int(row[6]) == 2017):
            print(row[1])
            k += 1
    if k == 0:
        print ('Ничего не найдено')