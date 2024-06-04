# Author: Rohtash Lakra

# import numpy as np
# import awkward as ak

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

