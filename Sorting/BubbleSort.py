#! /usr/bin/env python3

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        
        # Last i elements are already in place
        for j in range(n - i - 1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", numbers)

bubble_sort(numbers)

print("Sorted array:", numbers)