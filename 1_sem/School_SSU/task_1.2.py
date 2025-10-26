n = int(input())
print('Что требуется сделать с данным числом?')
print('1. найти процент от введённого числа')
print('2. увеличить число на какой-то процент')
print('3. уменьшить число на какой-то процент')
ans = int(input())
if 1 > ans > 3:
    print('Действие выбрано неверно')
else:
    percent = float(input())
    if percent < 0:
        print('Ошибка. Введите неотрицательное значение процента.')
    elif ans == 1:
        print(n * percent / 100)
    elif ans == 2:
        print(n * (100 + percent) / 100)
    elif ans == 3:
        print(n * (100 - percent) / 100)