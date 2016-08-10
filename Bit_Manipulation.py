# Cracking the coding interview - C5 - Bit Manipulation
# Stuart Bradley
# 05-08-2016

# Inject one binary number into another, between positions.
# Doesn't use bitwise operations because fuck it. 
def exercise_1(N, M, i, j):
	position = i+1
	str_N = list(str(N))
	for bit in reversed(str(M)):
		str_N[-position] = bit
		position += 1
	return int("".join(str_N))

# Decimal number to binary.
def exercise_2(decimal_number):
	binary = "."
	while decimal_number > 0:
		r = decimal_number * 2
		if r >= 1:
			binary += "1"
			decimal_number = r - 1
		else:
			binary += "0"
			decimal_number = r
	return binary

# Determine bit to flip to make longest sequence of 1s.
def exercise_3(sequence):
	zero_pos = []
	max_length = 0
	sequence = list(sequence)
	for i,char in enumerate(sequence):
		if char == "0":
			zero_pos.append(i)

	for i in zero_pos:
		tmp_sequence = sequence[:]
		tmp_sequence[i] = 1
		length = 0
		for char in tmp_sequence:
			if char == "0":
				length = 0
			else:
				length += 1
			if length > max_length:
				max_length = length
	return max_length

# Make biggest and smallest binary numbers.
def exercise_4(sequence):
	bits = sequence.count("1")
	biggest = int(sequence, 2)
	while True:
		biggest += 1
		binary = "{0:b}".format(biggest)
		if binary.count("1") == bits:
			biggest = binary
			break

	smallest = int(sequence, 2)
	while True:
		smallest -= 1
		binary = "{0:b}".format(smallest)
		if binary.count("1") == bits:
			smallest = binary
			break
	return (smallest, biggest)

# Check number of bits required to go from one number to another.
def exercise_6(n1, n2):
	count = 0
	c = n1 ^ n2 
	while c != 0:
		count += 1
		c = c & (c-1)
	return count

# Pairwise bit swap.
def exercise_7(sequence):
	sequence = list(sequence)
	for i in range(0,len(sequence) - 1,2):
		tmp = sequence[i]
		sequence[i] = sequence[i+1]
		sequence[i+1] = tmp
	return "".join(sequence)

# Draw a horizontal line on a screen.
def exercise_8(screen, width, x1, x2, y):
	chunks = [screen[x:x+width] for x in range(0, len(screen), width)]
	for i in range(x1,x2+1):
		chunks[y][i] = 1
	screen = []
	for chunk in chunks:
		screen.extend(chunk)
	return screen