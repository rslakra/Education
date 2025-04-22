#
# Author: Rohtash Lakra
#

# import numpy as np
# import awkward as ak

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

    print()


# Print Fibonacci Series of N numbers
# fib(1000)


def is_prime(n):
    if n <= 1:
        return False

    if n > 1:
        for num in range(2, n):
            if (n % num) == 0:
                return False

    return True


# Print N prime numbers
def prime(n):
    for num in range(1, n):
        # print(num)
        if is_prime(num):
            print(num)


# prime(5)


# Print N prime numbers
def primes(n):
    ctr = 0
    while ctr < n:
        for num in range(1, n * n):
            if ctr == n:
                break

            if is_prime(num):
                print(num)
                ctr += 1


# primes(10)

# Print N prime numbers
def get_primes(n):
    primes = []
    while len(primes) < n:
        for num in range(1, n * n):
            if len(primes) == n:
                break

            if is_prime(num):
                primes.append(num)

    return primes


# print(get_primes(5))

from string import ascii_lowercase


def get_primes_mapping_with_ascii_lowercase():
    alpha_primes = {}
    primes = get_primes(26)

    index = 0
    for letter in ascii_lowercase:
        # print(f"index:{index}, letter:{letter}")
        alpha_primes[letter] = primes[index]
        index += 1

    return alpha_primes


# print(get_primes_mapping_with_ascii_lowercase())

def is_anagram(left, right):
    alpha_primes = get_primes_mapping_with_ascii_lowercase()

    left_result = 1
    for letter in left.lower():
        if letter.isalpha():
            left_result *= alpha_primes[letter]

    # print(left_result)

    right_result = 1
    for letter in right.lower():
        if letter.isalpha():
            right_result *= alpha_primes[letter]

    # print(right_result)

    return left_result == right_result


def cache_key(*args):
    return "_".join(str(arg) for arg in args if arg is not None)



text = """

It was named after the fresh water dolphin native to the Amazon river. I wanted something short, unusual, and with at least some kind of connection to Amazon. Boto seemed to fit the bill.

"""


def build_dict(words):
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    return words_count


def print_dict(words):
    print("\n")
    for word in words:
        print(f"{word} : {words[word]}")


words = text.lower().split()
print(words)
word_dict = build_dict(words)
# print_dict(build_dict(words))
print(word_dict)

# build array using numpy
# import numpy as np
# buckets = np.array([])
# buckets = np.array([])
# print(buckets)
# fill array
# for word in word_dict:
#     index = buckets[word]
#     buckets[index].append(word)

# print(len(buckets))

# print(buckets.index)

# for i in range(10):
#     print(type(i))
#     buckets.append(i)

# buckets.append(1, "hi")
# print(buckets)

# arr = ak.ArrayBuilder()
# print(arr)



print(__name__)
# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
# However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'.
# Using this fact, you can discern which is the case at run-time and alter behavior accordingly:
if __name__ == '__main__':
    print()
    cache_key_result = cache_key(1, "apple", 3.14)
    print(f"cache_key_result={cache_key_result}")
    print()
    batch_id = None
    cache_key_result = cache_key("status", 16, batch_id)
    print(f"cache_key_result={cache_key_result}")

    batch_id = '22232d64d51b55749857db721a06b962'
    cache_key_result = cache_key("status", 16, batch_id)
    print(f"cache_key_result={cache_key_result}")

    # print(is_anagram("left", "f9?Le1T"))

    print()
    fruits = ["apple", "banana", "orange"]
    print(fruits)
    print(list(enumerate(fruits)))
    print(hash(enumerate(fruits)))
    print(id(enumerate(fruits)))

    print()
    loud_fruits = [fruit.upper() for fruit in fruits]
    print(loud_fruits)

    print()
    print(list(enumerate(loud_fruits)))
    print(hash(enumerate(loud_fruits)))
    print(id(enumerate(loud_fruits)))
    print("\n")

    print()
    input = 97
    print(f"input:{input}, str:{str(input)}, ascii:{ascii(input)}, oct:{oct(input)}")
    print(f"hex:{hex(input)}, bin:{bin(input)}, chr:{chr(input)}")
    print()

    print("\n")
    for index in range(1, 10, 2):
        print(index)
    print()

    input = 16
    print(f"input={input}")
    if input % 2 == 0:
        result = True
    else:
        result = False
    print(f"result={result}")

    value = None
    if not value:
        print(f'value={value}')
    else:
        print('None')
    print()

    if value is None:
        print('value is None')
    else:
        print(f'value={value}')
    print()

    print()
    for id in list(range(1, 5)):
        key = cache_key('key', str(id))
        print(f"key={key}")
    print()
    print(f"{cache_key('key', str(300))}")
    print()


