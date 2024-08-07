def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
result = linear_search([10,23,203,45,78], 45)
print(f"Linear search: Item found at index {result}." if result != -1 else "Item not found.")