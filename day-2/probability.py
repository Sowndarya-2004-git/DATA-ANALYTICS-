import random

def roll_die(num_rolls, target_number):
    count = 0
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        if roll == target_number:
            count += 1
    probability = count / num_rolls
    return probability

# Number of times to roll the die
num_rolls = 10000
# Target number to calculate probability for
target_number = 3

# Calculate probability
probability = roll_die(num_rolls, target_number)

print(f"The probability of rolling a {target_number} is approximately {probability:.4f}")