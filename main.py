# Cracking the coding interview - main tests class
# Stuart Bradley
# 02-08-2016

import unittest
import Arrays_And_Strings
import Linked_Lists

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

if __name__ == '__main__':
	unittest.main()