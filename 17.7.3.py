per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада '))
per_cent_list = list(per_cent.values())
deposit= []
for i in per_cent_list:
    deposit.append(int(i* money/100))
print(deposit)

#Находим максимальную сумму, которую можно заработать

max_earning= max(deposit)
print('Максимальная сумма заработка: ', max_earning)