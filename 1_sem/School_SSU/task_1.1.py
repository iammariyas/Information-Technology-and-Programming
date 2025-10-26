print('Введите название кинотеатра:')
cinema = input()
print('Введите название фильма:')
film = input()
print('Выберите номер подходящего времени сеанса:')
print('1. 13:30')
print('2. 16:45')
print('3. 20:00')
ans = int(input())

fl = True
if 1 > ans > 3:
    fl = False
    print('Ошибка. Похоже, такого сеанса не существует.')
elif ans == 1:
    time = '13:30'
elif ans == 2:
    time = '16:45'
elif ans == 3:
    time = '20:00'

if fl:
    print(f'Вы успешно забронировали билеты в кинотеатр «{cinema}» на фильм «{film}».')
    print(f'Сеанс начинается в {time}. Приятного просмотра!')