#
# Author: Rohtash Lakra
# Reference: https://realpython.com/python-logging/
#
import logging
from datetime import datetime

"""
Some of the commonly used parameters for basicConfig() are the following:

level: The root logger will be set to the specified severity level.
filename: This specifies the file.
filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
format: This is the format of the log message.

References:
- https://docs.python.org/3/library/logging.html#logging.basicConfig
- https://docs.python.org/3/library/logging.html#logrecord-attributes
- https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

"""

# Pattern: %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
# logFormat = f"%(asctime)s [%(thread)d:%(threadName)s] [%(process)d-%(processName)s] [%(levelname)8s] - (%(name)s:%(filename)s:%(lineno)d) - %(message)s"
logFormat = f"%(asctime)s %(threadName)s [%(levelname)8s] (%(processName)s:%(name)s:%(filename)s:%(lineno)d) - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="a", format=logFormat,
                    datefmt="%m-%d-%Y %H:%M:%S.%z")

UTF_8 = 'utf-8'
LOG_LEVEL = logging.DEBUG
DEFAULT_LOG_FORMAT = "[%(asctime)s] [%(process)d] [%(levelname)s] - %(message)s"
REQUEST_ID_LOG_FORMAT = "[%(asctime)s] [%(process)d] [%(levelname)s] [%(request_id)s] - %(message)s"
DETAILED_LOG_FORMAT = "[%(asctime)s] [%(process)d] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s"

DATE_FORMAT_TZ = "%Y-%m-%d %H:%M:%S %z"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT_MSEC = "%Y-%m-%d %H:%M:%S.%f,%03d"

# Configure app default loggers
logging.basicConfig(level=LOG_LEVEL, format=DETAILED_LOG_FORMAT, force=True)
# logging.config.fileConfig(fname='logger.ini', disable_existing_loggers=False)

# # get logger for filename
logger = logging.getLogger(__name__)


class AppLogger:
    _log_format = f"%(asctime)s %(threadName)s [%(levelname)8s] (%(processName)s:%(name)s:%(filename)s:%(lineno)d) - %(message)s"

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="a", format=self._log_format,
                            datefmt="%m-%d-%Y %H:%M:%S.%z")

        # logger.info("AppLogger()")

    @classmethod
    def add_handler(cls, logger: logging.Logger):
        # Create log handlers
        cls.console_handler = logging.StreamHandler()
        cls.file_handler = logging.StreamHandler("app.log")

        # add log level
        cls.console_handler.setLevel(logging.DEBUG)
        cls.file_handler.setLevel(logging.INFO)

        # Add handlers to logger
        logger.addHandler(cls.console_handler)
        logger.addHandler(cls.file_handler)

    @classmethod
    def getLogger(cls, name):
        # get logger for filename
        logger = logging.getLogger(name)
        cls.add_handler(logger)

        return logger

    # def show(self, message):
    #     logger.debug(f"message={message}")


# logger = AppLogger.getLogger(__name__)


def test_logs():
    logger.info("Start")
    logger.info(f"Testing logs")
    logger.warning("End")


logger.info(f"\nStarting: ${__file__}")
# logHelp = LogHelp()
# logger.show("Hi, Roh")
logger.debug("DEBUG Message")
logger.info("INFO Message")
logger.warning("WARNING Message")
logger.error("ERROR Message")
# logger.fatal(f"Log Message : {str(logging.FATAL)}")
logger.critical("CRITICAL Message")
test_logs()
logger.info(f"Ended")


def getClassName(self) -> str:
    """Returns the name of the class."""
    return type(self).__name__


class EnterExitLog(object):

    def __init__(self, funcName):
        self.funcName = funcName

    def __enter__(self):
        logger.debug(f"=> {getClassName(self)}-{self.funcName}()")
        self.startTime = datetime.now()
        return self

    def __exit__(self, type, value, tb):
        logger.debug(f"<= {getClassName(self)}-{self.funcName}() took {datetime.now() - self.startTime} second(s).\n")


def timer_decorator(func):
    def func_wrapper(*args, **kwargs):
        with EnterExitLog(func.__name__):
            return func(*args, **kwargs)

    return func_wrapper
