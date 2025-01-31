import matplotlib.pyplot as plt
import numpy as np

# QuickSort with animation
def quicksort_animation(arr, low, high, x, amount):
    if low < high:
        pi = partition(arr, low, high, x, amount)
        quicksort_animation(arr, low, pi - 1, x, amount)
        quicksort_animation(arr, pi + 1, high, x, amount)

def partition(arr, low, high, x, amount):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        plt.bar(x, arr, color=['red' if i == j or j == high else 'blue' for i in range(amount)])
        plt.pause(0.001)
        plt.clf()
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            plt.bar(x, arr, color=['red' if i == j else 'blue' for i in range(amount)])
            plt.pause(0.001)
            plt.clf()
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    plt.bar(x, arr, color=['red' if i == high or i == i + 1 else 'blue' for i in range(amount)])
    plt.pause(0.001)
    plt.clf()
    return i + 1

# Bubble Sort with animation
def bubble_sort_animation(arr, x, amount):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            plt.bar(x, arr, color=['red' if k == i or k == j else 'blue' for k in range(amount)])
            plt.pause(0.001)
            plt.clf()
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Insertion Sort with animation
def insertion_sort_animation(arr, x, amount):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            plt.bar(x, arr, color=['red' if k == j else 'blue' for k in range(amount)])
            plt.pause(0.001)
            plt.clf()
            j -= 1
        arr[j + 1] = key
        plt.bar(x, arr, color=['red' if k == j + 1 else 'blue' for k in range(amount)])
        plt.pause(0.001)
        plt.clf()

# Selection Sort with animation
def selection_sort_animation(arr, x, amount):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            plt.bar(x, arr, color=['red' if k == min_idx or k == j else 'blue' for k in range(amount)])
            plt.pause(0.001)
            plt.clf()
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plt.bar(x, arr, color=['red' if k == i or k == min_idx else 'blue' for k in range(amount)])
        plt.pause(0.001)
        plt.clf()

# Merge Sort with animation
def merge_sort_animation(arr, x, amount):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_animation(left, x, amount)
        merge_sort_animation(right, x, amount)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            plt.bar(x, arr, color=['red' if k == i else 'blue' for k in range(amount)])
            plt.pause(0.001)
            plt.clf()
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            plt.bar(x, arr, color=['red' if k == i else 'blue' for k in range(amount)])
            plt.pause(0.001)
            plt.clf()
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            plt.bar(x, arr, color=['red' if k == j else 'blue' for k in range(amount)])
            plt.pause(0.001)
            plt.clf()
            k += 1

# Generate random data
amount = 25
rand_list = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

# Create subplots for sorting algorithms
plt.figure(figsize=(15, 10))

# First subplot: Bubble Sort
plt.subplot(2, 3, 1)
plt.title("Bubble Sort")
bubble_sort_arr = rand_list.copy()
bubble_sort_animation(bubble_sort_arr, x, amount)

# Second subplot: Quick Sort
plt.subplot(2, 3, 2)
plt.title("Quick Sort")
quicksort_arr = rand_list.copy()
quicksort_animation(quicksort_arr, 0, len(rand_list) - 1, x, amount)

# Third subplot: Insertion Sort
plt.subplot(2, 3, 3)
plt.title("Insertion Sort")
insertion_sort_arr = rand_list.copy()
insertion_sort_animation(insertion_sort_arr, x, amount)

# Fourth subplot: Selection Sort
plt.subplot(2, 3, 4)
plt.title("Selection Sort")
selection_sort_arr = rand_list.copy()
selection_sort_animation(selection_sort_arr, x, amount)

# Fifth subplot: Merge Sort
plt.subplot(2, 3, 5)
plt.title("Merge Sort")
merge_sort_arr = rand_list.copy()
merge_sort_animation(merge_sort_arr, x, amount)

plt.show()
