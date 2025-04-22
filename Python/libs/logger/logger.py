# Author: Rohtash Lakra
import sys
import logging
import inspect

# configure logger
# [%(asctime)s] : [%(levelname)s] : %(name)s : %(message)s
# 2024-04-23 17:22:14,691 [DEBUG] - [__main__] : Staring application ...
# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
# https://docs.python.org/3/library/logging.html
# FORMAT = "%(asctime)s [%(levelname)-5s] - [%(name)s] : %(message)s"
# "%(asctime)s [%(levelname)8s] - [%(threadName)s-%(thread)d:%(name)s:%(filename)s (%(lineno)d)] : %(message)s"
# '%(asctime)s %(clientip)-15s %(user)-8s %(message)s '
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)8s] - [%(threadName)s-%(thread)d:%(filename)s (%(lineno)d)] : %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# consoleHandler = logging.StreamHandler(stream=sys.stdout)
# logFormatter = logging.Formatter("[%(asctime)s] : [%(levelname)s] : %(name)s : %(message)s")
# # Register the formatter to the stdout handler
# consoleHandler.setFormatter(logFormatter)
# logging.basicConfig(filename="myapp.log", level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# logger.addHandler(consoleHandler)
# logger.addHandler(logging.StreamHandler(stream=sys.__file__))


# method to count lenght of text
def count_length(text):
    logger.info(f"{inspect.stack()[0][3]}()")
    logger.info(f"count_lenth:{len(text)}")

# Starting point of application
if __name__ == '__main__':
    logger.debug("Staring application ...")
    text = """
    This module defines functions and classes which implement a flexible event logging system for applications and libraries.
    """
    count_length(text)
    logger.debug("Ending application ...")
