def foo(a):
    index_a = a.index(max(a))
    changes = [x * 10 for x in a[index_a + 1:] if x % 2 != 0]
    del a[index_a + 1:]
    a.extend(changes)

s = [1, 2, 3, 70, 1, 3, 24, 35, 11, 6]
foo(s)
print(s)