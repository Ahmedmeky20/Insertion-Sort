import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while i >= 0:
            comparisons += 1

            if arr[i] > key:
                arr[i + 1] = arr[i]
                shifts += 1
                i = i - 1
            else:
                break

        arr[i + 1] = key

    return arr, comparisons, shifts


numbers = [7, 3, 9, 2, 5]

print("Original Array:", numbers)

sorted_numbers, comparisons, shifts = insertion_sort(numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Shifts:", shifts)

print("--- Sorted Input ---")

numbers = [1, 2, 3, 4, 5]

sorted_numbers, comparisons, shifts = insertion_sort(numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Shifts:", shifts)


print("--- Reverse Sorted Input ---")

numbers = [5, 4, 3, 2, 1]

sorted_numbers, comparisons, shifts = insertion_sort(numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Shifts:", shifts)

print("\n--- Random Input ---")

numbers = [7, 2, 9, 1, 5]

sorted_numbers, comparisons, shifts = insertion_sort(numbers)

print("Sorted Array:", sorted_numbers)
print("Comparisons:", comparisons)
print("Shifts:", shifts)

numbers = [7, 3, 9, 2, 5]

start_time = time.time()

insertion_sort(numbers)

end_time = time.time()

running_time = end_time - start_time

print("Running Time:", running_time)


print("\n--- Testing 100 Elements ---")

numbers = list(range(100))

start_time = time.time()

insertion_sort(numbers)

end_time = time.time()

running_time = end_time - start_time

print("Number of Elements:", len(numbers))
print("Running Time:", running_time)

print("\n--- Testing 100 Reverse Elements ---")

numbers = list(range(100, 0, -1))

start_time = time.time()

insertion_sort(numbers)

end_time = time.time()

running_time = end_time - start_time

print("Number of Elements:", len(numbers))
print("Running Time:", running_time)

print("\n--- Testing 100 Random Elements ---")

numbers = [random.randint(1, 1000) for i in range(100)]

start_time = time.time()

insertion_sort(numbers)

end_time = time.time()

running_time = end_time - start_time

print("Number of Elements:", len(numbers))
print("Running Time:", running_time)

print("\n--- Sorted Input: Different Sizes ---")

sizes = []
sorted_times = []

for size in range(100, 5001, 100):

    numbers = list(range(size))

    start_time = time.time()

    insertion_sort(numbers)

    end_time = time.time()

    running_time = end_time - start_time

    sizes.append(size)
    sorted_times.append(running_time)

    print("Size:", size, "| Time:", running_time)

print("\n--- Reverse Sorted Input: Different Sizes ---")

reverse_times = []

for size in range(100, 5001, 100):

    numbers = list(range(size, 0, -1))

    start_time = time.time()

    insertion_sort(numbers)

    end_time = time.time()

    running_time = end_time - start_time

    reverse_times.append(running_time)

    print("Size:", size, "| Time:", running_time)

print("\n--- Random Input: Different Sizes ---")

random_times = []

for size in range(100, 5001, 100):

    numbers = [random.randint(1, 10000) for i in range(size)]

    start_time = time.time()

    insertion_sort(numbers)

    end_time = time.time()

    running_time = end_time - start_time

    random_times.append(running_time)

    print("Size:", size, "| Time:", running_time)


linear_reference = [
    sorted_times[-1] * (size / sizes[-1])
    for size in sizes
]

quadratic_reference = [
    reverse_times[-1] * (size / sizes[-1]) ** 2
    for size in sizes
]

# Plot Experimental Results
plt.figure(figsize=(10, 6))

plt.plot(sizes, sorted_times, label="Sorted Input")
plt.plot(sizes, reverse_times, label="Reverse Sorted Input")
plt.plot(sizes, random_times, label="Random Input")

# Plot Theoretical Complexity
plt.plot(sizes, linear_reference, "--", label="O(n)")
plt.plot(sizes, quadratic_reference, "--", label="O(n^2)")

# Graph Labels
plt.xlabel("Number of Elements")
plt.ylabel("Running Time (seconds)")

plt.title("Empirical Analysis of Insertion Sort")

plt.legend()
plt.grid()

# Save Graph
plt.savefig("insertion_sort_analysis.png", dpi=300)

# Display Graph
plt.show()