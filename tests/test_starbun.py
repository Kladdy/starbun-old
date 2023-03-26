import unittest
from starbun.test import super_tester

class TestStarbun(unittest.TestCase):

	def test_starbun(self):
		super_tester()
		self.assertEqual(1+1, 2)

unittest.main()