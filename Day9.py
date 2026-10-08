import logging
# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)

numbers = [64, 34, 25, 12, 22, 11, 90]

logger.info(f"Original List: {numbers}")

sorted_numbers = sorted(numbers)
logger.info(f"Using sorted(): {sorted_numbers}")

numbers.sort()
logger.info(f"Using sort(): {numbers}")

numbers.sort(reverse=True)
logger.info(f"Descending: {numbers}")


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

logger.info(f"Test Data: {data}")
logger.info(f"Bubble Sort   : {bubble_sort(data)}")
logger.info(f"Selection Sort: {selection_sort(data)}")
logger.info(f"Insertion Sort: {insertion_sort(data)}")

trace = [5, 3, 8, 1]

logger.info("Bubble Sort Trace")
logger.info(f"Start: {trace}")

for i in range(len(trace)):
    for j in range(len(trace) - i - 1):
        if trace[j] > trace[j + 1]:
            trace[j], trace[j + 1] = trace[j + 1], trace[j]

    logger.info(f"Pass {i + 1}: {trace}")

logger.info("Complexity Summary")
logger.info("Built-in Sort  : O(n log n)")
logger.info("Bubble Sort    : O(n²)")
logger.info("Selection Sort : O(n²)")
logger.info("Insertion Sort : O(n²)")