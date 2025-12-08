# load in text data from file
with open('day1.txt', 'r') as file:
    data = file.read()

# split the data into a list of numbers
numbers = data.split()

current = 50
answer = 0

for number in numbers:

	num = int(number[1:]) % 100
	if number[0] == 'L':
		if current - num < 0:
			current = 100 - (num - current)
		else:
			current -= num
	if number[0] == 'R':
		if current + num > 99:
			current = current + num - 100
		else:
			current += num

	print(current)
	if current == 0:
		answer += 1

print(answer)