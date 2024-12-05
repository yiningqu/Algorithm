# last element as pivot

def QuickSort(A, l, r):
    # Base case: if the array has one or no elements, no need to sort
    if l >= r:
        return 0

    # Number of comparisons is the length of the subarray minus one
    num_comparisons = r - l

    # Pre-processing step to swap the last element with the first
    A[l], A[r] = A[r], A[l]

    # Partition the array and get the new pivot index
    p_index = Partition(A, l, r)

    # Recursively sort the two parts
    num_comparisons += QuickSort(A, l, p_index - 1)
    num_comparisons += QuickSort(A, p_index + 1, r)

    return num_comparisons

def Partition(A, l, r):
    p = A[l]  # The pivot is now the first element after the pre-processing step
    i = l + 1

    for j in range(l + 1, r + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    # Place the pivot in its correct position
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

# The function can be called with the array and the indices of its first and last elements:
# (Assuming 'array' is your input array loaded from the file)
# total_comparisons = QuickSort(array, 0, len(array) - 1)



with open("/Users/yiningqu/Desktop/研究生/algorithm/Quicksort/Quicksort", "r") as file:
    array = [int(line.strip()) for line in file]
    
total_comparisons = QuickSort(array, 0, len(array) - 1)
print(total_comparisons)