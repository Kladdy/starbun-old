import unittest
from starbun.logger import logger

class TestStarbun(unittest.TestCase):

	def test_starbun(self):
		logger.info("info")
		logger.warn("warn")
		logger.error("error")
		logger.debug("debug")
		logger.fatal("fatal")

unittest.main()