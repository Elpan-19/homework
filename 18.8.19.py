ticket_num = int(input('Введите кол-во билетов: '))
ticket_price = 0

for i in range(ticket_num):
    i += 1
    age = int(input('Введите возраст посетителя: '))

    if age < 18:
        ticket_price += 0

    elif 18 <= age < 25:
        ticket_price += 990

    else:
        ticket_price += 1390

if ticket_num > 3:
    ticket_price = ticket_price - ((ticket_price/100) * 10)
    print(f'Сумма к оплате: {ticket_price} рублей, с учетом скидки 10%, т.к Вы регистрируете более 3х человек')

else:
    print(f'Сумма к оплате: {ticket_price} рублей')
