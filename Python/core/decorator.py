#
# Author: Rohtash Lakra
#
import time


def logtime(func):
    def wrapper(*args, **kwargs):
        print("Before")
        date_format = '%Y/%m/%d %T %Z'
        start_time = time.time()  # Start time
        print(f'{func.__name__}() started at={time.strftime(date_format)}')
        result = func(*args, **kwargs)  # Execute the function
        print("After")
        end_time = time.time()  # End time
        execution_time = round(end_time - start_time, 2)  # Calculate execution time
        print(f'{func.__name__}() ended at={time.strftime(date_format)} and took = {execution_time} seconds')

        return result

    return wrapper


@logtime
def hello():
    print("Hello, Function")
    time.sleep(5)


hello()
