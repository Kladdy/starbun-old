from starbun.logger import logger
from starbun.defaults import get_value, KEY_PROJECTS_PATH
import os
import sys

class Experiment: 
    def __init__(self, label, description=None, path=None):
        if not label:
            raise ValueError("Experiment label cannot be empty")
        if path == "":
            raise ValueError("Experiment path cannot be an empty string")
        self.label = label
        self.description = description
        self.path = self.get_path(path)

        # Make sure project path folder exists
        os.makedirs(self.path, exist_ok=True)

        logger.info(f"Experiment {self.label} initialized", experiment_label=self.label)
        if self.description:
            logger.info(f"Experiment {self.label} description: {self.description}", experiment_label=self.label)
        logger.info(f"Experiment path: '{self.path}'", experiment_label=self.label)

    def get_path(self, path):
        path = get_value(KEY_PROJECTS_PATH, path, experiment_label=self.label)
        
        # If the path is the current working directory, get the full name of it
        if path == "./":
            path = os.getcwd()

        # Add the experiment label to the end
        path = f"{path}/{self.label}"

        return path
