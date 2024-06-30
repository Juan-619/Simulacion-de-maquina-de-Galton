import matplotlib.pyplot as plt
import random

def simulate_galton_machine(num_balls=3000, num_levels=12):
    """
    Simulates a Galton machine with the given number of balls and levels.

    Parameters:
    num_balls (int): Number of balls to simulate.
    num_levels (int): Number of levels in the Galton machine.

    Returns:
    list: A list with the count of balls in each final container.
    """
    # Initialize the containers
    results = [0] * (num_levels * 2 + 1)

    # Simulate the trajectory of each ball
    for _ in range(num_balls):
        position = 0
        for _ in range(num_levels):
            # Randomly decide which way the ball falls
            position += 1 if random.random() > 0.5 else -1

        # Increment the corresponding container
        results[position + num_levels] += 1

    return results

def plot_histogram(results):
    """
    Plots a histogram of the given results.

    Parameters:
    results (list): List with the count of balls in each container.
    """
    plt.bar(range(len(results)), results)
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.title('Galton Machine Histogram')
    plt.show()

def main():
    """
    Runs the Galton machine simulation and plots the results.
    """
    results = simulate_galton_machine()
    plot_histogram(results)

if __name__ == "__main__":
    main()
