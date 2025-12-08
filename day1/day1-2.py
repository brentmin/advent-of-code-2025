# load in text data from file
with open('day1.txt', 'r') as file:
    data = file.read()

# split the data into a list of numbers
numbers = data.split()

current = 50
answer = 0
50 - 51 == 99

for number in numbers:

	num = int(number[1:])
	answer += num // 100
	num = num % 100
	should_add = current != 0
	if number[0] == 'L':
		if current - num < 0:
			current = 100 - (num - current)
			if current != 0 and should_add:
				answer += 1
		else:
			current -= num
	if number[0] == 'R':
		if current + num > 99:
			current = current + num - 100
			if current != 0 and should_add:
				answer += 1
		else:
			current += num

	if current == 0:
		answer += 1


print(answer)