import unittest

class MyTest(unittest.TestCase):

	def test_abc(self):
		print("hello")

	def test_def(self):
		print("world")

if __name__ == "__main__":
	unittest.main()
