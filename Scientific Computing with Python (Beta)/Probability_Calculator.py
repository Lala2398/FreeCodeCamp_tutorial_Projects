import copy
import random

class Hat:
    def __init__(self, **kwargs):
        """
        Initializes the Hat class with a variable number of arguments specifying the number of balls of each color.
        Each color and its count are converted into a list of strings stored in the contents attribute.
        """
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)  # Add 'count' number of balls of 'color' to the contents list.

    def draw(self, num_balls):
        """
        Draws a specified number of balls randomly from the hat.
        If the number of balls to draw exceeds the available balls, all balls are returned and removed from the hat.
        """
        if num_balls > len(self.contents):
            drawn_balls = self.contents.copy()  # Return a copy of all balls.
            self.contents.clear()  # Clear all balls from the hat.
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)  # Randomly select the specified number of balls.
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove the drawn balls from the contents.
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Conducts an experiment to estimate the probability of drawing a specified set of balls from a hat.

    Parameters:
    - hat: A Hat object containing the initial set of balls.
    - expected_balls: A dictionary specifying the desired balls and their counts.
    - num_balls_drawn: The number of balls to draw in each experiment.
    - num_experiments: The total number of experiments to perform.

    Returns:
    - The estimated probability of drawing the expected balls.
    """
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a copy of the hat to avoid modifying the original.
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw the specified number of balls.
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1  # Count the occurrences of each color in the drawn balls.

        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:  # Check if the drawn balls meet the expected criteria.
                success = False
                break

        if success:
            success_count += 1  # Increment the success count if the criteria are met.

    probability = success_count / num_experiments  # Calculate the probability of success.
    return probability

# Example usage
hat = Hat(blue=5, red=4, green=2)
probability = experiment(
    hat=hat,
    expected_balls={'red': 1, 'green': 2},
    num_balls_drawn=4,
    num_experiments=2000
)

print("Probability:", probability)  #Probability: 0.086
