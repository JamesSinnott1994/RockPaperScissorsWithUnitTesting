# Unittest library
import unittest

# We want to test all the moves in our Rock/Paper/Scissors game
import moves


# We're going to write our tests into what is known as a TestCase
class MoveTests(unittest.TestCase):
	def setUp(self):
		"""This method will get called before each of our
		tests, so any code we put in here will always have
		a fresh state"""
		# Python has to do more work as it has to instantiate
		# these variables every time, but we get to write less code!
		self.rock = moves.Rock()
		self.paper = moves.Paper()
		self.scissors = moves.Scissors()

	# Naming convention "test_ ...."
	def test_five_plus_five(self):
		# "assert" makes sure that whatever comes after it is true
		assert 5 + 5 == 10

	def test_one_plus_one(self):
		# "assert" makes sure that whatever comes after it is true
		assert not 1 + 1 == 3

	def test_equal(self):
		# Asserts that self.rock is equal to a new (other) rock instance
		# See "setUp" method
		self.assertEqual(self.rock, moves.Rock())

	def test_not_equal(self):
		self.assertNotEqual(self.rock, self.paper)

	def test_rock_better_than_scissors(self):
		self.assertGreater(self.rock, self.scissors)

	def test_paper_worse_than_scissors(self):
		self.assertLess(self.paper, self.scissors)

	def test_rock_is_instance(self):
		self.assertIsInstance(self.rock, moves.Rock)

# If we run the file directly, run the unitests that are in here
if __name__ == '__main__':
	unittest.main()