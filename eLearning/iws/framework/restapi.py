#
# Author: Rohtash Lakra
#
# Status Code

import requests
import time

def measure_ttfb(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    ttfb = (end_time - start_time) * 1000  # Convert to milliseconds
    return ttfb

url = "https://www.example.com"
ttfb = measure_ttfb(url)
print(f"TTFB for {url}: {ttfb:.2f} ms")