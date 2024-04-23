import os, json

files = []
l = []
files += os.listdir('transactions')
for i in files:
    f = open(f"{'transactions'}/{i}")
    l.append(json.loads(f.read()))
temp = []
a = l.copy()
for i in l:
    if i['hash'].startswith('000') and i['hash'].endswith('000'):
        print(f"№1. номер: {i['index']}", f"автор: {i['transactions'][-1]['to']}", sep='\t')
a = sorted(a, key=lambda x: x['index'])
d = dict()
for i in a:
    if i['index'] not in d:
        d[i['index']] = 1
    else:
        d[i['index']] += 1

fd = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(fd) - ключ/значение (индекс/количество повторов)
ad = 1  # счётчик длины
lads = []  # хранилище длин форков
lk = []  # временное хранилище цепочки форка
frks = []  # форки (только индексы)
for i in range(1, len(fd)):  # начинаем от единицы для второго условного оператора

    if fd[i][1] != 2:  # если все форки закончились
        lk.append(fd[i - 1][0])  # то же самое, что и на 41 строке
        lads.append(ad)  # то же самое
        frks.append(lk)  # то же самое
        break  # потому что форки закончились

    if fd[i][0] == fd[i - 1][0] + 1:  # если форк продолжается (17, 18, 19, ...) (с этой операции всё начинается)
        lk.append(fd[i - 1][0])  # фактически - временное хранилище для одного форка ()
        ad += 1  # счётчик длины

    else: # если форк закончился (17, 18, 19; 29, ...) (срабатывает на "29")
        lk.append(fd[i - 1][0])  # добавляем последнее значение
        lads.append(ad)  # в массив добавляется длина
        frks.append(lk)  # добавляем массив форков (только индексы)
        lk = [] # сброс "хранилища"
        ad = 1  # сброс счётчика длины

lads = sorted(lads)  # длины
frks = sorted(frks, key=lambda x: len(x))  # сортировка по длине форков (для 3-его задания)

print("№2. Длина наименьшего форка: ", lads[0])
print("№3. Номер первого блока в форке наименьшей длины: ", frks[0][0])
print("№4. Длина наибольшего форка: ", lads[-1])
c = 1
l = []
s = []
s = sorted(list(set(s)))[0:-1]

mfork = frks[-1]  # форк наибольшей длины (5-ое задание)
l = []
for i in a:
    if i['index'] == mfork[-1]:  # потому что в mfrok только индексы
        l.append([i['pre_hash'], i['timestamp']])
k = []
c = 1
l = sorted(l, key=lambda x: x[1])  # понять, что является отброшенным форком (timestmap должен быть ниже)
print(f"№5. Хэш последнего блока в отброшенной ветке форка наибольшей длины: {l[-1][0]}")
print("№6. Количество форков, произошедших в системе: ", len(frks))

for i in a:
    for j in i['transactions']:
        if j['from'] == 'SYSTEM':
            s.append(j['value'])
            if i['index'] == 71:
                print("№7. Размер вознаграждения за создание блока №71: ", j['value'])

indt = []
frgd = []
ddsf = dict()
for i in a:
    if i['index'] not in indt:
        indt.append(i['index'])
        frgd.append(i)

for i in frgd:
    for j in i['transactions']:
        if j['from'] == 'SYSTEM':
            if j['value'] not in ddsf:
                ddsf[j['value']] = 1
            else:
                ddsf[j['value']] += 1

gdfd = list(ddsf.values())[2:-1]
print("№8. Период сокращения размера вознаграждения за создание блока (каждые n блоков):", gdfd[0])

adsa = (list(ddsf.keys())[2:-1])
kd = round(adsa[1]/adsa[0], 2)  # коэффициент сокращения
print("№9. Коэффициент сокращения вознаграждения за выработку блока:", kd)
nagr = adsa[-1]
final_res = 0.09
numb = len(adsa)
# Считается, что каждая награда повторяется 17 раз. Т.е., чтобы узнать номер блока, достаточно умножить его на 17

while round(nagr, 2) != round(0.09, 2):
    nagr *= kd
    numb += 1

print("№10. № блока, в котором в будущем размер вознаграждения впервые окажется равен 0,09:", numb * 17)

df = list()
gf = list()
ka = list()

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if (a[i]['index'] == a[j]['index']):  # проверка только на форки
            if a[i]['timestamp'] < a[j]['timestamp']: # Укажите блоки, в которых в поле secret_info встречается дополнительная информация, блоки откинутых форков не учитываются. Я считаю, что откинутый форк - это где timestamp больше
                ka.append(a[i])
            else:
                ka.append(a[j])

indx = [i
        for j in frks
        for i in j]

for i in a:
    if i['index'] not in indx:  # проверка не только на форки
        ka.append(i)

ka = sorted(ka, key=lambda x: x['index'])

for i in ka:
    if len(i['secret_info']) != 0:
        df.append(str(i['index']))
        gf.append(str(i['secret_info']))

print(f"№11. Блоки, в которых в поле secret_info встречается дополнительная информация:", ", ".join(df))
print(f"№12. Полученная информация в порядке её появления:", " ".join(gf))
print(f"№13. Шестнадцатеричная форма представления ключевой строки: ", bytes.fromhex("".join(gf)).decode('utf-8'))

