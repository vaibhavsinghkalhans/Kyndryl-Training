numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original List:", numbers)

sorted_numbers = sorted(numbers)
print("Using sorted():", sorted_numbers)

numbers.sort()
print("Using sort():", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)


def bubble_sort(arr):
    arr = arr.copy()

    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(arr):
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


data = [64, 34, 25, 12, 22, 11, 90]

print("\nTest Data:", data)
print("Bubble Sort   :", bubble_sort(data))
print("Selection Sort:", selection_sort(data))
print("Insertion Sort:", insertion_sort(data))

trace = [5, 3, 8, 1]

print("\nBubble Sort Trace")
print("Start:", trace)

for i in range(len(trace)):
    for j in range(len(trace) - i - 1):
        if trace[j] > trace[j + 1]:
            trace[j], trace[j + 1] = trace[j + 1], trace[j]

    print(f"Pass {i + 1}:", trace)

print("\nComplexity Summary")
print("Built-in Sort  : O(n log n)")
print("Bubble Sort    : O(n²)")
print("Selection Sort : O(n²)")
print("Insertion Sort : O(n²)")