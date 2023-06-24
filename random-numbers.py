import random

# Generate 5 random numbers
random_numbers = [random.randint(100, 10000) for i in range(5)]

# Print the random numbers
print("List of randomly generated numbers:", random_numbers)

# Ask user to input the order
order = input("Enter the order of the numbers (asc/des): ").lower()

# Check if the order is valid
while order != "asc" and order != "des":
    order = input("Invalid order. Please enter a valid order (asc/des): ").lower()

# Sort the numbers in the selected order
if order == "asc":
    sorted_numbers = sorted(random_numbers)
else:
    sorted_numbers = sorted(random_numbers, reverse=True)

# Ask user to input the sorted numbers
input_numbers = input("Enter the sorted numbers separated by commas: ").split(",")

# Convert the input numbers to integers
input_numbers = [int(num.strip()) for num in input_numbers]

# Check if the input numbers match the sorted numbers
if input_numbers == sorted_numbers:
    print("Correct")
else:
    print("Not correct")