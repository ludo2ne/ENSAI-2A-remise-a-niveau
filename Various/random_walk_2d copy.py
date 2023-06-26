import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def random_walk_2d(n_steps):
    """
    Generate a 2D random walk with a given number of steps.

    Parameters:
    - n_steps (int): Number of steps in the random walk.

    Returns:
    - positions (list of tuples): List of (x, y) positions visited during the random walk.
    """
    x = 0
    y = 0
    positions = [(0, 0)]

    for _ in range(n_steps):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1

        positions.append((x, y))

    return positions


# Generate 200 random walks with 10000 steps each
n_points = 100
n_steps = 10000
random_walks = [random_walk_2d(n_steps) for _ in range(n_points)]

# Initialize the figure and axes
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(-500, 500)
ax.set_ylim(-500, 500)

# Create an empty scatter plot
scat = ax.scatter([], [], edgecolors='black', s=5)


def update(frame):
    # Update the scatter plot with the new positions
    x = [pos[0] for pos in random_walks[frame]]
    y = [pos[1] for pos in random_walks[frame]]
    scat.set_offsets(list(zip(x, y)))


# Create the animation with a delay of 100 milliseconds between frames
ani = animation.FuncAnimation(fig, update, frames=n_steps, interval=300)

plt.title("Simultaneous Random Walk")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
