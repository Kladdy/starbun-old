import unittest
from starbun.logger import logger

class TestStarbun(unittest.TestCase):

	def test_starbun(self):
		experiment = "PROJECT"
		trial = "T1"
		run = "R1"
		logger.info("this is a test")
		logger.warn("this is a test")
		logger.error("this is a test")
		logger.debug("this is a test")
		logger.fatal("this is a test")

		logger.info("this is a test", experiment_label=experiment)
		logger.warn("this is a test", experiment_label=experiment, trial_label=trial)
		logger.error("this is a test", experiment_label=experiment, trial_label=trial, run_label=run)
		logger.debug("this is a test", trial_label=trial, run_label=run)
		logger.fatal("this is a test")

unittest.main()