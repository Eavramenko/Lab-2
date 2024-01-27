#Авраменко Екатерина Алексеевна ИСУ: 408103
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

list_author=[]
list_title=[]
list_year=[]
result=[]
with open('books-en.csv', encoding = 'latin-1') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        list_author.append(row['Book-Author'])
        list_title.append(row['Book-Title'])
        list_year.append(row['Year-Of-Publication'])
for i in range(20):
    result.extend([str(i+1), '; ', list_author[i], '; ', list_title[i], '; ', list_year[i], '\n'])

file = open('result.txt', 'w')
file.writelines(result)
file.close()

with open('books-en.csv', encoding = 'latin-1') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        if int(row['Downloads']) > max_dow:
            max_dow = int(row['Downloads'])
        if len(popularity) < 20:
            while max_dow >= 0:
                if row['Downloads'] == str(max_dow):
                        popularity.append(row['Book-Title'])
                max_dow -= 1

        check.append(row['Publisher'])

        for i in check:
            if i not in publisher:
                publisher.append(i)

print('Перечень издательств: ', publisher)
print('20 самых популярных книг: ')
for i in range(20):
    print(popularity[i])