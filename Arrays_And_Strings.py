# Cracking the coding interview - C1 - Arrays And Strings
# Stuart Bradley
# 02-08-2016

import itertools

# Check for uniqueness.
def exercise_1(string):
	unique_chars = set()
	for c in string:
		if c in unique_chars:
			return False
		else:
			unique_chars.add(c)
	return True

# Check for uniqueness without additional structures (O(n) space).
def exercise_1_set(string):
	if len(set(string)) < len(string):
		return False
	else:
		return True

# Check if one string is a permutation of another.
def exercise_2(string1, string2):
	# Create HashMap.
	char_locations = {}
	for i in range(len(string2)):
		c = string2[i]
		if c in char_locations:
			char_locations[c].append(i)
		else:
			char_locations[c] = [i]

	# Go through string1
	for c in string1:
		if c not in char_locations:
			return False
		else:
			char_locations[c].pop()
			if char_locations[c] == []:
				del char_locations[c]

	if len(char_locations) > 0:
		return False
	else:
		return True

# Replace spaces with '%20'
def exercise_3(string):
	string = list(string)
	for i in range(len(string)):
		if string[i] == " ":
			string[i] = "%%20"
	return "".join(string)

# Find palindromes.
def exercise_4(string):
	# Create HashMap.
	number_odd = 0
	number_even = 0
	char_counts = {}
	for c in string:
		if c in char_counts:
			char_counts[c] += 1
			# Check if count is even.
			if char_counts[c] % 2 == 0:
				number_even += 1
				number_odd -= 1
			else:
				number_even -= 1
				number_odd += 1
		else:
			char_counts[c] = 1
			number_odd += 1

	# Check if palindromes are possible.
	if len(string) % 2 == 0 and number_odd != 0:
		return False
	elif len(string) % 2 == 1 and number_odd != 1:
		return False

	odd = ""
	side_1 = []
	side_2 = []

	for c,count in char_counts.items():
		temp_count = count
		if count % 2 == 1:
			odd = c
			temp_count -= 1

		chars_per_side = int(temp_count / 2)
		tmp = [c]*chars_per_side
		side_1.extend(tmp)
		side_2.extend(tmp)

	palindromes = []

	palindrome_side = itertools.permutations(range(len(side_1)), len(side_1))
	for subset in palindrome_side:
		palindrome = ""
		for i in subset:
			palindrome += side_1[i]
		palindrome += odd
		for i in reversed(subset):
			palindrome += side_2[i]

		palindromes.append(palindrome)

	return True

# Check if two strings are no more than one edit apart.
def exercise_5(string1, string2):
	if len(string1) > len(string2):
		string1,string2 = string2,string1
	distances = range(len(string1) + 1)
	for index2,char2 in enumerate(string2):
		newDistances = [index2+1]
		for index1,char1 in enumerate(string1):
			if char1 == char2:
				newDistances.append(distances[index1])
			else:
				newDistances.append(1 + min((distances[index1], distances[index1+1], newDistances[-1])))
		distances = newDistances

	if distances[-1] > 1: 
		return False
	else:
		return True

# Compress string.
def exercise_6(string):
	compressed_string = ""
	current_char = string[0]
	count = 0
	for c in string:
		if c is not current_char: 
			compressed_string += current_char + str(count)
			current_char = c
			count = 1
		else:
			count += 1
	compressed_string += current_char + str(count)

	if len(compressed_string) >= len(string):
		return string
	else:
		return compressed_string

# Rotate a matrix 90.
def exercise_7(matrix):
	size = len(matrix)
	layer_count = int(size / 2)

	for layer in range(0, layer_count):
		first = layer
		last = size - first - 1

		for element in range(first, last):
			offset = element - first

			top = matrix[first][element]
			right_side = matrix[element][last]
			bottom = matrix[last][last-offset]
			left_side = matrix[last-offset][first]

			matrix[first][element] = left_side
			matrix[element][last] = top
			matrix[last][last-offset] = right_side
			matrix[last-offset][first] = bottom

	return matrix

# Create zero rows and columns when a zero is found. 
def exercise_8(matrix):
	columns_to_zero = set()
	for row_index in range(len(matrix)):
		zeroRow = False
		for cell_index in range(len(matrix[row_index])):
			if matrix[row_index][cell_index] == 0:
				columns_to_zero.add(cell_index)
				zeroRow = True
				for backtracked_index in range(0,cell_index):
					matrix[row_index][backtracked_index] = 0
			elif zeroRow or (cell_index in columns_to_zero):
				matrix[row_index][cell_index] = 0
	return matrix

# Determine if one string is a rotation of another.
def exercise_9(string1, string2):
	l1 = len(string1)
	l2 = len(string2)

	if l1 != l2:
		return False

	# subString call.
	pos1 = 0
	pos2 = string2.find(string1[pos1])
	if pos2 == -1:
		return False

	while(pos1 < len(string1) - 1):
		pos1 += 1
		if pos2 + 1 < len(string2):
			pos2 += 1
		else:
			pos2 = 0
		if string1[pos1] != string2[pos2]:
			return False

	return True