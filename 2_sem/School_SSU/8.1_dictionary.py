# Найти все слова, встречающиеся столько же раз, сколько первое число.
with open('../../../school_SSU/input.txt') as f:
    data = f.read().split()

w_counter = {}
for elem in data:
    if not elem.lstrip('-').isdigit():
        w_counter[elem] = w_counter.get(elem, 0) + 1
print(w_counter)

first_num = 0
for i in data:
    if i.lstrip('-').isdigit():
        first_num = int(i)
        break
print(first_num)

res = [key for key, value in w_counter.items() if value == first_num]
print(*res)