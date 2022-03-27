import random

spaces_histogram = {}

for i in range(1, 41):
    spaces_histogram[i] = 0

for i in range(1,1000):
    answer = random.randint(1,6) + random.randint(1,6)
    spaces_histogram[answer] += 1

print(spaces_histogram)