# Задача6: Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
day_num  = int(input('Введите номер дня недели '))
def day_week(num):
    week = ['пн', 'вт', 'ср', 'чт' , 'пт' , 'сб' , 'вс']
    if (0> num > 7):
        print('такого дня недели нет')
    elif (5 < num <= 7):
        print(f'да, {week[num-1]}')
    else:
        print (f'{week[num-1]}, нет')

day_week(day_num)