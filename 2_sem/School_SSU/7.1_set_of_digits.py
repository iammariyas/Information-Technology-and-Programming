# 16

nums = [x for x in input().split()]
digits = set(range(10))

for num1, num2 in zip(nums, nums[1:]):
    pair_digits = {int(x) for x in set(num1 + num2)}
    missing_digits = digits - pair_digits
    print(f'{num1}, {num2} не встречающиеся цифры: {missing_digits}')
