import time

print("===== Binary Search Algorithm =====")

# Get input from user
size = int(input("Enter the number of elements: "))
numbers = []

for i in range(size):
    value = int(input(f"Enter value {i + 1}: "))
    numbers.append(value)

# Arrange elements in ascending order
numbers.sort()

print("\nSorted Array:", numbers)

# Search element
target = int(input("Enter the element to find: "))

# Start execution timer
start_time = time.perf_counter()

left = 0
right = size - 1
result = -1

while left <= right:
    center = (left + right) // 2

    if numbers[center] == target:
        result = center
        break
    elif target > numbers[center]:
        left = center + 1
    else:
        right = center - 1

# Stop execution timer
end_time = time.perf_counter()

# Display result
if result != -1:
    print(f"\nElement {target} found at index {result}.")
else:
    print(f"\nElement {target} was not found.")

# Execution time
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.10f} seconds")

# Time complexity
print("Best Time Complexity   : O(1)")
print("Average Time Complexity: O(log n)")
print("Worst Time Complexity  : O(log n)")