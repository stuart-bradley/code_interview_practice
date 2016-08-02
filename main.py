# Cracking the coding interview - main tests class
# Stuart Bradley
# 02-08-2016

import unittest
import Arrays_And_Strings

class Test_Arrays_And_Strings(unittest.TestCase):
	longMessage = True

	def test_exercise_1(self):
		test_cases = {
			"abc" : "abc",
			"abc" : "adc"
		}
		for key, value in test_cases.items():
			with self.subTest(key=key, value=value):
				self.assertEqual(key, Arrays_And_Strings.exercise_1(value))

if __name__ == '__main__':
	unittest.main()