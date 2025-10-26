# 14
with open('../../../../school_SSU/input.txt', 'r') as f:
    lines = f.readlines()
    num_set = []
    for line in lines:
        if line.strip():
            nums = set(int(x) for x in line.strip().split())
            num_set.append(nums)

    for num1, num2 in zip(num_set, num_set[1:]):
        unique_numbers = set(num1) - set(num2)
        print(f'{num1}, {num2} Уникальные числа в первой строке: {unique_numbers}')
