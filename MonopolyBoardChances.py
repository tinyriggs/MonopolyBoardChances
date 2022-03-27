import random
import matplotlib.pyplot as plt

spaces_histogram = {}
x_tick = []

for i in range(1, 41):
    spaces_histogram[i] = 0
    x_tick.append(i)

answer = 0

for i in range(1,31):
    answer = answer + (random.randint(1,6) + random.randint(1,6))
    if answer > 40:
        answer = answer - 40
    spaces_histogram[answer] += 1



def plot_graph():
    x = []
    y = []
    for key in spaces_histogram:
        x.append(key)
        y.append(spaces_histogram[key])
    plt.bar(x, y)
    plt.xticks(x_tick)
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.title("my graph")
    plt.show()

plot_graph()