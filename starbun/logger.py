from termcolor import colored

def format_labels(experiment_label=None, trial_label=None, run_label=None):
    if not experiment_label and not trial_label and not run_label:
        return None

    labels = [experiment_label, trial_label, run_label]
    label = f"{' / '.join([label for label in labels if label])} |"
    return colored(label, "grey")

class Logger:
    def __init__(self, name):
        if not name:
            raise ValueError("Logger name cannot be empty")
        self.name = name

    def log(self, message, level_string, level_color, color=None,
            experiment_label=None, trial_label=None, run_label=None):
        name_string = colored(f"[{self.name}]", "cyan")
        level_string = colored(f"{str.ljust(level_string, 6)}", level_color, attrs=["bold"])
        labels = format_labels(experiment_label=experiment_label, trial_label=trial_label, run_label=run_label)
        prefix = " ".join(filter(lambda item: item is not None, [name_string, level_string, labels]))

        if color:
            print(prefix, colored(message, color))
        else:
            print(prefix, message)

    def info(self, message, experiment_label=None, trial_label=None, run_label=None):
        self.log(message, level_string="info", level_color="blue", experiment_label=experiment_label, trial_label=trial_label, run_label=run_label)

    def warn(self, message, experiment_label=None, trial_label=None, run_label=None):
        self.log(message, level_string="warn", level_color="yellow", experiment_label=experiment_label, trial_label=trial_label, run_label=run_label)

    def error(self, message, experiment_label=None, trial_label=None, run_label=None):
        self.log(message, level_string="error", level_color="red", experiment_label=experiment_label, trial_label=trial_label, run_label=run_label)

    def debug(self, message, experiment_label=None, trial_label=None, run_label=None):
        self.log(message, level_string="debug", level_color="grey", experiment_label=experiment_label, trial_label=trial_label, run_label=run_label)

    def fatal(self, message, experiment_label=None, trial_label=None, run_label=None):
        self.log(message, level_string="fatal", level_color="magenta", experiment_label=experiment_label, trial_label=trial_label, run_label=run_label)

logger = Logger("Starbun")