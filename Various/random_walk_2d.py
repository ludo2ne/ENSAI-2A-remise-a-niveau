import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


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


# Generate a 2D random walk with 1000 steps
n_steps = 10000
positions = random_walk_2d(n_steps)

# Extract x and y coordinates for plotting
x = [pos[0] for pos in positions]
y = [pos[1] for pos in positions]

# Generate a list of colors with a gradient from blue to red
colors = mcolors.LinearSegmentedColormap.from_list(
    'gradient', ['blue', 'red'], len(x))

# Plot the random walk with gradient colors
plt.scatter(x, y, c=range(len(x)), cmap=colors, s=2)
plt.title("2D Random Walk")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label='Step')
plt.show()
