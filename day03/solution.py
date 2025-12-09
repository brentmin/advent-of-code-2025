with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read()

lines = data.split()

def larget_2_digit_number(line):
	largest = 0
	largest_i = -1
	for i in range(len(line) - 1):
		if int(line[i]) > largest:
			largest = int(line[i])
			largest_i = i
	
	second_largest = 0
	for i in range(largest_i + 1, len(line)):
		if int(line[i]) > second_largest:
			second_largest = int(line[i])
	
	return int(str(largest) + str(second_largest))

answer = 0
for line in lines:
	answer += larget_2_digit_number(line)
print(answer)