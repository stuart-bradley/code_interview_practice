# Cracking the coding interview - C3 - Stack and Queues
# Stuart Bradley
# 04-08-2016

from collections import deque
from random import randint

# 3.1: Create multiple stacks on the same list. 
class exercise_1_and_2:
	main_array = []
	offset = 0
	
	def __init__(self):
		self.stack_offset = exercise_1_and_2.offset
		exercise_1_and_2.offset += 1
		self.top_pos = self.stack_offset
		self.size = 0
		exercise_1_and_2.main_array.extend([None,None])

	def pop(self):
		if exercise_1_and_2.main_array[self.top_pos] == None:
			return None
		item = exercise_1_and_2.main_array[self.top_pos]
		exercise_1_and_2.main_array[self.top_pos] = None
		self.top_pos -= self.stack_offset
		self.size -= 1
		return item

	def push(self, item):
		next_free_pos = self.top_pos + self.stack_offset
		if next_free_pos > len(exercise_1_and_2.main_array) - 1:
			extra_space = [None] * len(exercise_1_and_2.main_array)
			exercise_1_and_2.main_array.extend(extra_space)
		exercise_1_and_2.main_array[next_free_pos] = item
		self.top_pos = next_free_pos
		self.size += 1

	def peek(self):
		return exercise_1_and_2.main_array[self.top_pos] 

	def is_empty(self):
		if self.size > 0:
			return False
		else:
			return True

	# 3.2: Return the bottom of the stack.
	def get_minimum(self):
		return exercise_1_and_2.main_array[self.stack_offset]

# Implement multiple stacks with max_size
class exercise_3:
	def __init__(self, max_size):
		self.stacks = [[]]
		self.current_stack = self.stacks[0]
		self.max_size = max_size

	def pop(self):
		return self.current_stack.pop()

	def pop_at(self, pos):
		return self.stacks[pos].pop()

	def push(self, item):
		if len(self.current_stack) >= self.max_size:
			self.stacks.append([])
			self.current_stack = self.stacks[-1]			
		self.current_stack.append(item)

	def peek(self):
		return self.current_stack[-1]

# Create a queue with two stacks.
class exercise_4():
	def __init__(self):
		self.add_stack = []
		self.remove_stack = []

	def remove(self):
		while self.add_stack:
			self.remove_stack.append(self.add_stack.pop())
		
		result = self.remove_stack.pop()

		# Reset stacks
		while self.remove_stack:
			self.add_stack.append(self.remove_stack.pop())

		return result

	def add(self, item):
		self.add_stack.append(item)

	def peek():
		while self.add_stack:
			self.remove_stack.append(self.add_stack.pop())
		
		result = self.remove_stack[-1]

		# Reset stacks
		while self.remove_stack:
			self.add_stack.append(self.remove_stack.pop())

		return result

# Sort stack.
def exercise_5(stack):
	tmp_stack = []
	while stack:
		# hold current variable and find location in tmp_stack.
		tmp = stack.pop()
		while tmp_stack and (tmp_stack[-1] > tmp):
			stack.append(tmp_stack.pop())
		tmp_stack.append(tmp)

	while tmp_stack:
		stack.append(tmp_stack.pop())

	return stack

# Create an animal shelter, where people can adopt the oldest cat or dog.
class exercise_6:
	def __init__(self):
		self.cats = deque()
		self.dogs = deque()

	def enqueue(self, animal):
		if animal == "dog":
			self.dogs.append(animal)
		elif animal == "cat":
			self.cats.append(animal)

	def dequeue_any(self):
		if len(self.dogs) > len(self.cats):
			return self.dogs.popleft()
		elif len(self.dogs) < len(self.cats):
			return self.cats.popleft()
		else:
			if randint(0,1) == 0:
				return self.dogs.popleft()
			else:
				return self.cats.popleft()

	def dequeue_cat(self):
		return self.cats.popleft()

	def dequeue_dog(self):
		return self.dogs.popleft()
