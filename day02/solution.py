with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# split the data into a list of numbers
numbers = data.split(',')

answer = 0

for number in numbers:
    # split the number into a list of numbers
    range_numbers = number.split('-')
    for i in range(int(range_numbers[0]), int(range_numbers[1]) + 1):
        mid_i = len(str(i)) // 2
        first_half = str(i)[:mid_i]
        second_half = str(i)[mid_i:]
        if first_half == second_half:
            answer += i
print(answer)