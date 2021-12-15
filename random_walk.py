# start

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def random_walk(w):
    increments = np.array([1, -1])
    random_increments = np.random.choice(increments, w, True)
    random_walks = np.cumsum(random_increments)
    return random_walks, random_increments


def init():
    line.set_data([], [])
    return line,


def animate(i):
    y = X[i]
    x_data.append(i)
    y_data.append(y)
    line.set_data(x_data, y_data)
    return line,


np.random.seed(1234)
x_data = []
y_data = []
# random walk
N = 30
X, epsilon = random_walk(N)
X = X * np.sqrt(1. / N)

fig = plt.figure(figsize=(21, 10))
ax = plt.axes(xlim=(1, N), ylim=(np.min(X) - 0.5, np.max(X) + 0.5))
line, = ax.plot([], [], lw=2, color='#0492C2')
ax.set_xticks(np.arange(1, N+1, 1))
ax.set_yticks(np.arange(np.min(X) - 0.5, np.max(X) + 0.5, 0.2))
ax.set_title('Stock price on investing market (Random Walk)', fontsize=22)
ax.set_xlabel('Days on market', fontsize=18)
ax.set_ylabel('Percentage of price change', fontsize=18)
ax.tick_params(labelsize=16)
ax.grid(True, which='major', linestyle='--', color='black', alpha=0.4)

# creates gif with rw
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=20, blit=True)
anim.save('random_investing.gif')
