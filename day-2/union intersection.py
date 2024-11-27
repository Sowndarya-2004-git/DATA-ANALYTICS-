def calculate_union(set_a, set_b):
    """Calculate the union of two sets."""
    return set_a.union(set_b)

def calculate_intersection(set_a, set_b):
    """Calculate the intersection of two sets."""
    return set_a.intersection(set_b)

def get_set_from_input(prompt):
    """Get a set of integers from user input."""
    while True:
        try:
            user_input = input(prompt)
            # Convert the input string to a set of integers
            return set(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

# Get user input for two sets
set_a = get_set_from_input("Enter elements of Set A separated by spaces: ")
set_b = get_set_from_input("Enter elements of Set B separated by spaces: ")

# Calculate union and intersection
union_result = calculate_union(set_a, set_b)
intersection_result = calculate_intersection(set_a, set_b)

# Print results
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union of A and B: {union_result}")
print(f"Intersection of A and B: {intersection_result}")