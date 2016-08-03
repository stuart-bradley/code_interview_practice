# Cracking the coding interview - C2 - Linked Lists
# Stuart Bradley
# 03-08-2016

# Linked lists hs been "faked" using normal lists.

from collections import deque

# Remove duplicates from linked list.
def exercise_1(linked_list):
	dups_to_remove = []
	unique_elems = set()
	for i in range(len(linked_list)):
		if linked_list[i] in unique_elems:
			dups_to_remove.append(i)
		else:
			unique_elems.add(linked_list[i])
	for index in sorted(dups_to_remove, reverse=True):
		del linked_list[index]

	return linked_list

# Remove duplicates inplace using sort.
def exercise_1_inplace(linked_list):
	# Sort in place.
	linked_list.sort()
	pos = 0
	current_char = ""
	while pos < len(linked_list):
		if linked_list[pos] != current_char:
			current_char = linked_list[pos]
		else:
			del linked_list[pos]
		pos += 1
	return linked_list

# Get kth last element.
def exercise_2(linked_list,k):
	kth_elements = deque(maxlen=k)
	for item in linked_list:
		kth_elements.append(item)
	return kth_elements.popleft()

# Remove internal node at position.
def exercise_3(linked_list,pos):
	if pos < len(linked_list) - 1:
		next_elem = linked_list[pos+1]
		linked_list[pos] = next_elem
		del linked_list[pos]
	return linked_list

# Partion list on element.
def exercise_4(linked_list,x):
	pivot = -1
	for i in range(len(linked_list)):
		if linked_list[i] == x and pivot == -1:
			pivot = i
		if linked_list[i] < x and pivot > -1:
			tmp = linked_list[i] 
			del linked_list[i]
			linked_list.insert(0,tmp)
	return linked_list

# Sum lists (Reverse).
def exercise_5_reverse(linked_list1, linked_list2):
	sum_str_1 = ""
	sum_str_2 = ""

	for item in linked_list1:
		sum_str_1 = str(item) + sum_str_1
	for item in linked_list2:
		sum_str_2 = str(item) + sum_str_2
	return [int(i) for i in reversed(str(int(sum_str_1) + int(sum_str_2)))]

# Sum lists (Forward).
def exercise_5_forward(linked_list1, linked_list2):
	sum_str_1 = ""
	sum_str_2 = ""

	for item in linked_list1:
		sum_str_1 += str(item)
	for item in linked_list2:
		sum_str_2 += str(item)
	return [int(i) for i in str(int(sum_str_1) + int(sum_str_2))]

# Check if linked list is a palindrome.
def exercise_6(linked_list):
	l = len(linked_list)
	halfway = int(l / 2)
	stack = []
	# Odd.
	if l % 2 == 1:
		for pos in range(len(linked_list)):
			if pos < halfway:
				stack.append(linked_list[pos])
			elif pos > halfway:
				elem = stack.pop()
				if elem != linked_list[pos]:
					return False
	# Even.
	else:
		for pos in range(len(linked_list)):
			if pos <= halfway:
				stack.append(linked_list[pos])
			else:
				elem = stack.pop()
				if elem != linked_list[pos]:
					return False
	return True

# Check if two linked lists intersect.
def exercise_7(linked_list1, linked_list2):
	if len(set(linked_list1) & set(linked_list2)) > 0:
		return True
	else:
		return False

# Loop detection.
def exercise_8(linked_list):
	unique_elems = set()
	for item in linked_list:
		if item in unique_elems:
			return item
		else:
			unique_elems.add(item)
	return None