import unittest
from fizzBuzz import fizzbuzz

class Test(unittest.TestCase):

	def test_simple_should_return_the_number(self):
		self.assertEqual(fizzbuzz(1), 1)
		self.assertEqual(fizzbuzz(2), 2)
		self.assertEqual(fizzbuzz(4), 4)

	def test_multiple_3_should_return_fizz(self):
		self.assertEqual(fizzbuzz(6), "fizz")
		self.assertEqual(fizzbuzz(9), "fizz")

	def test_multiple_5_should_return_buzz(self):
		self.assertEqual(fizzbuzz(5), "buzz")
		self.assertEqual(fizzbuzz(10), "buzz")
	
	def test_multiple_3_and_5_should_return_fizzbuzz(self):
		self.assertEqual(fizzbuzz(15), "fizzbuzz")
		self.assertEqual(fizzbuzz(30), "fizzbuzz")

if __name__ == '__main__':
	unittest.main()