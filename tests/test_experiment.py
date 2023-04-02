import unittest
from starbun.experiment import Experiment

class TestExperiment(unittest.TestCase):
	def test_experiment(self):
	
		e = Experiment(label="Sample project", description="This is a test")

unittest.main()