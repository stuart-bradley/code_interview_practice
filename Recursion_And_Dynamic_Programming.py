# Cracking the coding interview - C8 - Recursion_And_Dynamic_Programming
# 10-08-2016

import collections
import re
import itertools

# Count the number of ways up n steps using 1, 2 or 3 step jumps.
def exercise_1(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	if n == 2:
		return 2
	memo = [1,1,2]
	for i in range(2,n):
		memo.append(memo[i-1]+memo[i-2]+memo[i-3])
	return memo[-1]

# Find and return path. 
def exercise_2(graph, start, end):
	queue = collections.deque()
	queue.append([start])
	while queue:
		path = queue.popleft()
		if path[-1] == end:
			return path
		for child in graph[path[-1]]:
			new_path = list(path)
			if child not in new_path:
				new_path.append(child)
				queue.append(new_path)
	return []

# Find magic index (l[i] = i).
# Handles duplicate values.
def exercise_3(magic_array):
	return exercise_3_rec(magic_array, 0, len(magic_array) - 1)

def exercise_3_rec(array, start, end):
	if (end < start):
		return -1

	mid_index = (start + end) // 2
	mid_val = array[mid_index]
	if mid_index == mid_val:
		return mid_index

	left_index = min(mid_index - 1, mid_val)
	left = exercise_3_rec(array, start, left_index)
	if left >= 0:
		return left

	right_index = max(mid_index + 1, mid_val)
	right = exercise_3_rec(array, right_index, end)
	return right

# Find subsets of a set.
def exercise_4(subset_set):
	subsets = {}
	for i in range(1, len(subset_set)):
		if i == 1:
			subsets[1] = []
			for item in subset_set:
				subsets[1].append([item])
		else:
			subsets[i] = []
			for subset in subsets[i-1]:
				for item in subsets[1]:
					if item[0] not in subset:
						subsets[i].append(subset+item)
	return [val for sublist in subsets.values() for val in sublist]

# Multiply two positive integers without *.
def exercise_5(n1, n2):
	res = 0
	for _ in range(n2):
		res += n1 
	return res

# Towers of Hanoi.
def exercise_6(n, source, aux, target):
	if n > 0:
		exercise_6(n - 1, source, target, aux)
		if source:
			target.append(source.pop())
		exercise_6(n - 1, aux, source, target)

# Permutations (no dups).
def exercise_7(string):
	permutations = {}
	for i in range(1, len(string)):
		if i == 1:
			permutations[1] = []
			for item in string:
				permutations[1].append(item)
		else:
			permutations[i] = []
			for subset in permutations[i-1]:
				for item in permutations[1]:
					if item[0] not in subset:
						permutations[i].append(subset+item)
	return [val for sublist in permutations.values() for val in sublist]

# Permutations (dups).
def exercise_8(string):
	permutations = {}
	occurances = {}
	for i in range(1, len(string)):
		if i == 1:
			permutations[1] = []
			for item in string:
				permutations[1].append(item)
				if item in occurances:
					occurances[item] += 1
				else:
					occurances[item] = 1
		else:
			permutations[i] = []
			for subset in permutations[i-1]:
				for item in permutations[1]:
					new_item = subset+item
					if occurances[item[0]] > subset.count(item[0]) and new_item not in permutations[i]:
						permutations[i].append(new_item)
	return [val for sublist in permutations.values() for val in sublist]

# Permutations of sets of brackets.
def exercise_9(n):
	permutations = {}
	for i in range(n+1):
		if i == 0:
			permutations[i] = {}
		elif i == 1:
			permutations[i] = {"()"}
		else:
			permutations[i] = set([])
			for config in permutations[i-1]:
				# After.
				permutations[i].add(config + "()")
				# Surround.
				for start,end in bracket_positions(config):
					start_string = config[:start]
					middle_string = config[start:end+1]
					end_string = config[end+1:]
					new_config = start_string + "(" + middle_string + ")" + end_string
					permutations[i].add(new_config)
	return list(permutations[i])

def bracket_positions(config):
	stack = []
	positions = []
	for i,bracket in enumerate(config):
		if bracket == "(":
			stack.append(("(",i))
		else:
			start = stack.pop()
			positions.append((start[1],i))
	for i in range(0, len(positions)):
		start, end = positions[i]
		current_end = end
		for j in range(i, len(positions)):
			start_next, end_next = positions[j]
			if start_next == current_end + 1:
				positions.append((start, end_next))
				current_end = end_next
	return positions

# paint_fill
def exercise_10(screen, position, new_colour):
	queue = collections.deque()
	queue.append(position)
	old_colour = screen[position[0]][position[1]]
	while queue:
		x,y = queue.popleft()
		if screen[x][y] == old_colour or screen[x][y] == new_colour:
			screen[x][y] = new_colour
			children = []
			for new_position in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
				x,y = new_position
				if 0 <= x < len(screen) and 0 <= y < len(screen[0]) and screen[x][y] != new_colour:
					queue.append(new_position)
	return screen

# Subset sum of money
def exercise_11(target, partial=[]):
	coins = [1,5,10,25]

	number_of_ways = []

	s = sum(partial)
	if s == target:
		return [partial]
	elif s > target:
		return []
	for i in range(len(coins)):
		n = coins[i]
		number_of_ways.extend(exercise_11(target, partial+[n]))
	return number_of_ways

# Eight queens problem - faster as a genetic algorithm.
def exercise_12(n):
	sols = 0
	cols = range(n)
	for vec in itertools.permutations(cols):
		if (n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))):
			sols += 1
	return sols

# Make the tallest possible stack of boxes
def exercise_13(boxes):
	boxes.sort(reverse=True)
	# Create stack.
	stack_main = []
	stack_aux = []
	stack_main.append(boxes.pop())
	while boxes:
		box = boxes.pop()
		while stack_main:
			top = stack_main[-1]
			if box[0] > top[0] and box[1] > top[1] and box[2] > top[2]:
				stack_main.append(box)
				break
			stack_aux.append(stack_main.pop())
		if not stack_main and box[0] > stack_aux[-1][0] and box[1] > stack_aux[-1][1] and box[2] > stack_aux[-1][2]:
			stack_main.append(box)
		while stack_aux:
			stack_main.append(stack_aux.pop())
	# Get height.
	print(stack_main)
	height = 0
	for box in stack_main:
		height += box[1]
	return height

# Calculate most ways brackets can make boolean string eval correctly.
def exercise_14(s, result, memo={}):
	if len(s) == 0:
		return 0
	if len(s) == 1:
		if s == "1" and result == True:
			return 1
		elif s == "0" and result == False:
			return 1
		else:
			return 0
	if str(result) + s in memo:
		return memo[str(result) + s]

	ways = 0
	for i in range(1, len(s), 2):
		c = s[i]
		left = s[0:i]
		right = s[i+1:]
		leftTrue = exercise_14(left, True, memo)
		leftFalse = exercise_14(left, False, memo)
		rightTrue = exercise_14(right, True, memo)
		rightFalse = exercise_14(right, False, memo)
		total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

		totalTrue = 0
		if c == '^':
			totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
		elif c == '&':
			totalTrue = leftTrue * rightTrue
		elif c == '|':
			totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse

		subWays = result if bool(totalTrue) else total - totalTrue
		ways += subWays

	memo[str(result)+s] = ways
	return ways