import logging
import sys


class Logger:
    def __init__(self, file_path: str):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setLevel(logging.DEBUG)
        self.stdout_handler.setFormatter(self.formatter)

        file_handler = logging.FileHandler(file_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(self.stdout_handler)
