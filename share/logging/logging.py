import logging
import sys


class Logs:
    def __init__(self, name_logger=None, log="warning"):
        self.name_logger = name_logger or 'ROOT'
        self.__level = self.__get_level(log)

        logging.basicConfig(stream=sys.stderr, level=self.__level)
        self.log = logging.getLogger(self.name_logger)

    @staticmethod
    def __get_level(log):
        levels = {
            'info': logging.INFO,
            'debug': logging.DEBUG,
            'warning': logging.WARNING,
            'error': logging.ERROR
        }

        return levels.get(log, logging.WARNING) if log else logging.WARNING
