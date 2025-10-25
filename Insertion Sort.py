## Uses the Insertion Sort algorithm to sort out numbers in their monotonically decreasing order. 
## It accepts user input of the list items, sorts them based on an insertion logic and displays the original list and the sorted list.

def insertion_sort_desc(arr):
    # going through each element starting from the second one
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # moving elements that are smaller than the current one to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # placing the current element in the correct position
        arr[j + 1] = key


# asking the user for the number of elements
n = int(input("Enter the number of elements: "))
arr = []

# taking the elements from the user
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

# showing the list before sorting
print("\nOriginal list:", arr)

# sorting the list in decreasing order
insertion_sort_desc(arr)

# showing the list after sorting
print("Sorted list (decreasing order):", arr)

print("Hello")