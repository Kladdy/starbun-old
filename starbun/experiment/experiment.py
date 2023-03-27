from starbun.logger import logger

class Experiment: 
    def __init__(self, label, description=None, path=None):
        if not label:
            raise ValueError("Experiment label cannot be empty")
        self.label = label
        self.description = description
        self.path = path

        logger.info(f"Experiment {self.label} initialized", experiment_label=self.label)
        if self.description:
            logger.info(f"Experiment {self.label} description: {self.description}", experiment_label=self.label)