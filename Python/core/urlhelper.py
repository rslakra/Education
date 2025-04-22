#
# Author: Rohtash Lakra
#
import sys
import logging
import requests

logger = logging.getLogger(__name__)

logger.debug("Initializing ...")
# python urlhelper.py https://httpbin.org/status/200
print()
try:
    logger.debug("sys.argv: {sys.argv}")
    print(sys.argv)
    response = requests.get(sys.argv[1])
except ConnectionError as ex:
    logger.error("Error: {ex}")
    print(f"{ex}")

print(f"{response.status_code} - {response.content}")
print()
logger.debug("Ended")

