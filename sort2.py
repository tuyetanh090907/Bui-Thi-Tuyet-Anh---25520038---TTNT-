import numpy as np
import time
import heapq

file_du_lieu = [
    "data/daytangdan.npy",
    "data/daygiamdan.npy",
    "data/daythuc1.npy",
    "data/daythuc2.npy",
    "data/daythuc3.npy",
    "data/daythuc4.npy",
    "data/daynguyen1.npy",
    "data/daynguyen2.npy",
    "data/daynguyen3.npy",
    "data/daynguyen4.npy",
]

#Quick Sort------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return (quick_sort(left) + middle + quick_sort(right))
    
#Merge Sort------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#Heap Sort------------------------------
def heap_sort(arr):
    n = len(arr)

    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1)

    for end in range(n - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(0, end - 1)
        
    return arr

#Numpy Sort------------------------------
def numpy_sort(arr):
    return np.sort(arr)

#Đo thời gian thực thi hàm sắp xếp    
def measure_time(func, arr):
    start = time.perf_counter()
    func(arr)
    return time.perf_counter() - start

#Chạy thử và in kết quả    
for file in file_du_lieu:
    print (f"\n Dataset: {file}")
    data = np.load(file)
    for name, func in [
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
        ("Heap Sort", heap_sort),
        ("Numpy Sort", numpy_sort)
    ]:
        t = measure_time(func, data.copy())
        print(f" {name:12s}: {t:.4f} giây")
    