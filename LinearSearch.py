import time

print("\n========== LINEAR SEARCH ==========")

# Read input
size = int(input("Enter number of elements: "))

numbers = []

print("\nEnter the elements:")
for count in range(size):
    value = int(input(f"Element {count + 1}: "))
    numbers.append(value)

search_value = int(input("\nEnter value to search: "))


# Linear Search Function
def search_element(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


# Start execution timer
start = time.perf_counter()

result = search_element(numbers, search_value)

# End execution timer
end = time.perf_counter()

execution_time = end - start


# Display result
print("\n---------- RESULT ----------")

if result != -1:
    print(f"Element {search_value} found.")
    print(f"Index     : {result}")
    print(f"Position  : {result + 1}")
else:
    print(f"Element {search_value} was not found.")

print(f"Execution Time: {execution_time:.10f} seconds")

print("\n---------- DAA ANALYSIS ----------")
print("Best Case     : O(1)")
print("Average Case  : O(n)")
print("Worst Case    : O(n)")
print("Space         : O(1)")