# Program to calculate Sum, Average, Maximum, and Minimum

# Take input from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate values
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Display results
print("\nResults")
print("-------")
print("Numbers :", numbers)
print("Sum     :", total)
print("Average :", average)
print("Maximum :", maximum)
print("Minimum :", minimum)