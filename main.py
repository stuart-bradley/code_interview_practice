# Cracking the coding interview - main tests class
# Stuart Bradley
# 02-08-2016

import unittest
import Arrays_And_Strings
import Linked_Lists
import Stacks_And_Queues
import Trees_And_Graphs
import Bit_Manipulation

class Test_Arrays_And_Strings(unittest.TestCase):
	longMessage = True

	def test_exercise_1(self):
		test_cases = {
			True : "abc",
			False : "add"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_1(value))
				self.assertEqual(key, Arrays_And_Strings.exercise_1_set(value))

	def test_exercise_2(self):
		test_cases = {
			True : ["abc","bca"],
			False : ["add", "abb"]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_2(value[0], value[1]))

	def test_exercise_3(self):
		test_cases = {
			 "a%%20b%%20c":"a b c",
			 "a%%20b%%20": "a b "
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_3(value))

	def test_exercise_4(self):
		test_cases = {
			True : "tactcoa",
			False : "acb"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_4(value))

	def test_exercise_5(self):
		test_cases = {
			True : ["pale","ple"],
			False : ["pale","bake"]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_5(value[0],value[1]))

	def test_exercise_6(self):
		test_cases = {
			"aabbcc" : "aabbcc",
			"a3b2" : "aaabb"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_6(value))

	def test_exercise_7(self):
		start = [[0,  1,  2], [3,  4,  5], [6,  7,  8]] 
		end = [[6,  3,  0], [7,  4,  1], [8,  5,  2]]
		self.assertEqual(end,Arrays_And_Strings.exercise_7(start))

	def test_exercise_8(self):
		start = [[1,  0,  1], [1,  1,  1], [1,  1,  1]] 
		end = [[0,  0,  0], [1,  0,  1], [1,  0,  1]] 
		self.assertEqual(end,Arrays_And_Strings.exercise_8(start))

	def test_exercise_9(self):
		test_cases = {
			True : ["erbottlewat", "waterbottle"],
			False : ["erbottlewat", "watexbottle"]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_9(value[0],value[1]))

class Test_Linked_Lists(unittest.TestCase):
	longMessage = True

	def test_exercise_1(self):
		test_cases = {
			(1,2,3) : [1,1,2,3],
			("hi","ho") : ["hi","ho","ho"]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(list(key), Linked_Lists.exercise_1(value))
				self.assertEqual(list(key), Linked_Lists.exercise_1_inplace(value))

	def test_exercise_2(self):
		test_cases = {
			"a" : [[2,2,"a",3],2],
			"b" : [[2,1,1,"b",3,3],3]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Linked_Lists.exercise_2(value[0],value[1]))

	def test_exercise_3(self):
		test_cases = {
			(1,2,4,5) : [[1,2,3,4,5],2],
			(1,2,3,4,5) : [[1,2,3,4,5],4]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(list(key), Linked_Lists.exercise_3(value[0],value[1]))

	def test_exercise_4(self):
		test_cases = {
			(1,2,6,6,5) : [[1,2,6,6,5],5],
			(5,1,2,6,6) : [[1,2,6,6,5],6]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(list(key), Linked_Lists.exercise_4(value[0],value[1]))

	def test_exercise_5(self):
		test_cases = {
			(2,1,9) : [[7,1,6],[5,9,2]]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(list(key), Linked_Lists.exercise_5_reverse(value[0],value[1]))
				self.assertEqual(list(key), list(reversed(Linked_Lists.exercise_5_forward(reversed(value[0]),reversed(value[1])))))

	def test_exercise_6(self):
		test_cases = {
			True : "abba",
			True : "aba"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Linked_Lists.exercise_6(value))

	def test_exercise_7(self):
		test_cases = {
			True : [["a","b","c"],["d","b","e"]],
			False : [["a","b","c"],["d","e","f"]]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Linked_Lists.exercise_7(value[0],value[1]))

	def test_exercise_8(self):
		test_cases = {
			"b" : ["a","b","c","b"],
			None : ["a","b","c"]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Linked_Lists.exercise_8(value))


class Test_Stacks_And_Queues(unittest.TestCase):
	longMessage = True

	def test_exercise_1_and_2(self):
		stack_a = Stacks_And_Queues.exercise_1_and_2()
		stack_b = Stacks_And_Queues.exercise_1_and_2()
		stack_c = Stacks_And_Queues.exercise_1_and_2()

		stack_a.push(1)
		stack_b.push(2)
		stack_c.push(3)

		a = stack_a.pop()
		b = stack_b.pop()
		c = stack_c.pop()

		test_cases = {
			1 : a,
			2 : b,
			3 : c
		}

		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, value)
		self.assertEqual(None, stack_a.get_minimum())

	def test_exercise_3(self):
		stacks = Stacks_And_Queues.exercise_3(2)

		stacks.push(1)
		stacks.push(2)
		stacks.push("a")

		first_pop = stacks.pop_at(0)

		self.assertEqual(2, first_pop)

	def test_exercise_4(self):
		queue = Stacks_And_Queues.exercise_4()

		queue.add(1)
		queue.add(2)
		result = queue.remove()

		self.assertEqual(1, result)

	def test_exercise_5(self):
		test_cases = {
			(4,3,2,1) : [4,3,2,1],
			(4,3,2,1) : [1,2,3,4]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(list(key), Stacks_And_Queues.exercise_5(value))

	def test_exercise_6(self):
		shelter = Stacks_And_Queues.exercise_6()

		shelter.enqueue("dog")
		shelter.enqueue("cat")
		shelter.enqueue("cat")

		animal = shelter.dequeue_any()
		dog = shelter.dequeue_dog()

		self.assertEqual("cat", animal)
		self.assertEqual("dog", dog)

class Test_Trees_And_Graphs(unittest.TestCase):
	longMessage = True

	def test_exercise_1(self):
		graph = {
			0 : [1,2],
			1 : [3],
			2 : [1],
			3 : [],
			4 : [3]
		}

		test_cases = {
			True : [graph, 0, 3],
			False : [graph, 0, 4]
		}

		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_1_DFS(value[0],value[1],value[2]))
				self.assertEqual(key, Trees_And_Graphs.exercise_1_BFS(value[0],value[1],value[2]))

	def test_exercise_2(self):
		test_cases = {
			"12345": [1,2,3,4,5]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_2(value).traverse_inorder())

	def test_exercise_3(self):
		test_cases = [
			[[[3],[2,4],[1,5]], {1: [], 2: [1], 3: [2, 4], 4: [5], 5: []}]
		]

		for test_case in test_cases:
			with self.subTest(key=test_case[0], value=test_case[1]):
				self.assertEqual(test_case[0], Trees_And_Graphs.exercise_3(test_case[1]))

	def test_exercise_4(self):
		test_cases = {
			True: {1: [], 2: [1], 3: [2, 4], 4: [5], 5: []},
			False: {1: [], 2: [1], 3: [2, 4], 4: [5], 5: [6], 6: [7], 7:[]}
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_4(value))

	def test_exercise_5(self):
		test_cases = {
			True: {1: [], 2: [1], 3: [2, 4], 4: [3.2,5], 5: [], 3.2:[]},
			False: {20: [], 2: [20], 3: [2, 4], 4: [3.2,5], 5: [], 3.2:[]}
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_5(value))

	def test_exercise_6(self):
		test_cases = {
			2: [{1: [], 2: [1], 3: [2, 4], 4: [3.2,5], 5: [], 3.2:[]},1],
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_6(value[0],value[1]))

	def test_exercise_7(self):
		test_cases = {
			(1,2,3) : [[1,2,3],[[1,2],[2,3],[1,3]]],
			(5,6,1,2,4,3) : [[1,2,3,4,5,6],[[1,4],[6,2],[2,4],[6,1],[4,3]]]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(list(key), Trees_And_Graphs.exercise_7(value[0],value[1]))

	def test_exercise_8(self):
		test_cases = [
			[3, {1: [], 2: [1], 3: [2, 4], 4: [5], 5: []},1,5]
		]

		for test_case in test_cases:
			with self.subTest(key=test_case[0], value=test_case[1]):
				self.assertEqual(test_case[0], Trees_And_Graphs.exercise_8(test_case[1],test_case[2],test_case[3]))

	def test_exercise_9(self):
		test_cases = {
			((2,1,3),(2,3,1)) : {1:[],2:[1,3],3:[3]},
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				key = [list(x) for x in key]
				self.assertEqual(key, Trees_And_Graphs.exercise_9(value))

	def test_exercise_10(self):
		test_cases = {
			True : [{1:[2,3],2:[4,5],3:[],4:[],5:[]},{2:[4,5],4:[],5:[]}],
			False : [{1:[2,3],2:[4,5],3:[],4:[],5:[]},{6:[7,8],7:[],8:[]}]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_10(value[0],value[1]))

	# Exercise 11 is a random test, and as such can be easily tested. 
	# However, with the tree representation used, is very trival.

	def test_exercise_12(self):
		test_cases = {
			2 : [{1:[[],0],2:[[3,5],0],3:[[1],0],4:[[2,6],0],5:[[],0],6:[[],0]},10]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Trees_And_Graphs.exercise_12(value[0],value[1]))

class Test_Bit_Manipulation(unittest.TestCase):
	longMessage = True

	def test_exercise_1(self):
		test_cases = {
			10001001100 : [10000000000, 10011,2,6]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Bit_Manipulation.exercise_1(value[0], value[1], value[2], value[3]))

	def test_exercise_2(self):
		test_cases = {
			".1011100001010001111010111000010100011110101110000101" : 0.72
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Bit_Manipulation.exercise_2(value))

	def test_exercise_3(self):
		test_cases = {
			8 : "11011101111",
			6 : "110111001111"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Bit_Manipulation.exercise_3(value))

	def test_exercise_4(self):
		test_cases = {
			('10100101', '10101001') : "10100110",
			('-11111111', '101111111') : "11111111"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Bit_Manipulation.exercise_4(value))

	# Exercise 5 happens on paper.
	# The answer is that the code checks if n is a power of 2.

	def test_exercise_6(self):
		test_cases = {
			2 : [29,15]
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Bit_Manipulation.exercise_6(value[0],value[1]))

	def test_exercise_7(self):
		test_cases = {
			"1010" : "0101"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Bit_Manipulation.exercise_7(value))

	def test_exercise_8(self):
		screen = [0] * 16
		result_screen = screen
		result_screen[0] = 1
		result_screen[1] = 1
		result_screen[2] = 1


		self.assertEqual(result_screen, Bit_Manipulation.exercise_8(screen,8,0,2,0))

if __name__ == '__main__':
	unittest.main()