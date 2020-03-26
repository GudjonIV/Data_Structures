from MyHashableKey import *
from random import Random
from time import time

filename = "words.txt"
words_list = []
with open(filename, "r") as f:
    for word in f:
        words_list.append(word.strip())

if __name__ == "__main__":
    start_time = time()
    size = 43
    key_list = [[0] * size for x in range(11)]
    rand = Random()
    for index, word in enumerate(words_list):
        # Concrete test: always returns same 
        concrete_index = hash(MyHashableKey(index, word)) % size
        key_list[0][concrete_index] += 1
        # Random test: returns average of 10 lists
        for list_index in range(1, 11):
            integer = rand.randint(0, len(words_list))
            rand_index = hash(MyHashableKey(integer, word)) % size
            key_list[list_index][rand_index] += 1

    difference = max(key_list[0]) - min(key_list[0])
    ratio = difference / max(key_list[0])
    print (key_list[0])
    print ("\nConcrete ratio:", ratio)
    rand_difference = 0
    avg_max = 0
    for lis_index in range(1, 11):
        rand_difference += max(key_list[lis_index]) - min(key_list[lis_index])
        avg_max += max(key_list[lis_index])
    rand_difference = rand_difference / (len(key_list) - 1)
    avg_max = avg_max / (len(key_list) - 1)
    rand_ratio = rand_difference / avg_max
    print ("\nRandom average ratio", rand_ratio)
    total_time = time() - start_time
    print ("Total time taken:", total_time)
    print ("Time ratio:", total_time / len(key_list))
