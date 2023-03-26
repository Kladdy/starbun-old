from termcolor import colored

class Logger:
    def __init__(self, name):
        if not name:
            raise ValueError("Logger name cannot be empty")
        self.name = name

    def log(self, message, color=None):
        name_string = colored(f"[{self.name}]", "cyan")
        if color:
            print(name_string, colored(message, color))
        else:
            print(name_string, message)

    def info(self, message):
        self.log(message, "blue")

    def warn(self, message):
        self.log(message, "yellow")

    def error(self, message):
        self.log(message, "red")

    def debug(self, message):
        self.log(message, "grey")

    def fatal(self, message):
        self.log(message, "magenta")

logger = Logger("Starbun")