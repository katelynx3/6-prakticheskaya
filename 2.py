emp = int(input('Какая у вас температура? '))
davlenie = int(input('Какое у вас верхнее давление? '))
pulse = int(input('Какой у вас пульс? '))

if 36 <= temp <= 37 and 110 <= davlenie <= 130 and 60 <= pulse <= 100:
    print('У вас нормальное состояние')
elif (temp == 35 or temp == 38) or (105 <= davlenie < 110 or 130 < davlenie <= 140) or (55 <= pulse < 60 or 100 < pulse <= 110):
    print('У вас легкое недомогание')
else:
    print('Вам нужен врач')
