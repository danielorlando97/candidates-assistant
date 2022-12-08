import time
import sys
import random


result = []
start = time.time()
for i in range(0, 10000):
    index = random.randint(0, len(result))
    result.insert(index, 0)

print('insert', time.time() - start)


result = [0] * 10000
start = time.time()
for i in range(0, 10000):
    index = random.randint(0, len(result)-1)
    result.pop(index)

print('pop', time.time() - start)

result = []
start = time.time()
for i in range(0, 10000):
    index = random.randint(0, len(result))
    result = result[:index] + [0] + result[index:]

print('manual', time.time() - start)