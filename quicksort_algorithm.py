import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Deterministic pivot: middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Randomly select pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    return time.time() - start

sizes = [1000, 5000, 10000, 20000]
distributions = {
    "Random": lambda n: [random.randint(0, n) for _ in range(n)],
    "Sorted": lambda n: list(range(n)),
    "Reverse": lambda n: list(range(n, 0, -1))
}

for dist_name, dist_func in distributions.items():
    print(f"\n--- {dist_name} Input ---")
    for n in sizes:
        arr = dist_func(n)
        t_det = measure_time(quicksort, arr)
        t_rand = measure_time(randomized_quicksort, arr)
        print(f"n={n:6} | Deterministic: {t_det:.5f}s | Randomized: {t_rand:.5f}s")
