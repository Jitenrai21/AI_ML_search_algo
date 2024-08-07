def binary_search(arr, target):
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            first = mid + 1
        elif (arr[mid] > target):
            last = mid -1
    return -1
        

array = [10, 20, 30, 40, 50, 60]
tar = 45
result = binary_search(array, tar)
print("Target not found!" if result == -1 else f"Your searched result is in index {result}.")
# print(f"Your searched result is in index {result}." if result != -1 else "Target not found.")