import unittest
from starbun.experiment import experiment

class TestExperiment(unittest.TestCase):

	def test_experiment(self):
		e = experiment.Experiment(label="PROJECT", description="This is a test", path="")

unittest.main()