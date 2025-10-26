# 15

lines = [x for x in input().split()]
res = []
for line in lines:
    set_symbol = set()
    set_repeat_symbol = set()
    for symbol in line:
        if symbol.isalpha():
            if symbol not in set_symbol:
                set_symbol.add(symbol)
            else:
                set_symbol.remove(symbol)
                set_repeat_symbol.add(symbol)
    res.append(set_repeat_symbol)
    print(f'{line} повторяющиеся буквы: {set_repeat_symbol}')
