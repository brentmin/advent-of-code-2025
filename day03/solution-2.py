with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read()

lines = data.split()

def larget_12_digit_number(line):
	result = ""
	last_i = 0
	for battery_offset in range(11, -1, -1):
		largest = 0
		largest_i = -1

		for i in range(last_i, len(line) - battery_offset):
			if int(line[i]) > largest:
				largest = int(line[i])
				largest_i = i
		
		last_i = largest_i + 1
		result += str(largest)
	
	return int(result)

answer = 0
for line in lines:
	answer += larget_12_digit_number(line)
print(answer)