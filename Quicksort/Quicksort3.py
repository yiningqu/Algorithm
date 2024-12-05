# use meidan as the pivot

def QuickSort(A, l, r):
    # Base case: if the array has one or no elements, no need to sort
    if l >= r:
        return 0

    # Choose pivot according to the median-of-three rule and move it to the first position
    median = median_of_three(A, l, r)
    A[l], A[median] = A[median], A[l]

    # Number of comparisons is the length of the subarray minus one
    num_comparisons = r - l

    # Partition the array and get the new pivot index
    p_index = Partition(A, l, r)

    # Recursively sort the two parts
    num_comparisons += QuickSort(A, l, p_index - 1)
    num_comparisons += QuickSort(A, p_index + 1, r)

    return num_comparisons

def Partition(A, l, r):
    p = A[l]
    i = l + 1

    for j in range(l + 1, r + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    # Place the pivot in its correct position
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

def median_of_three(A, l, r):
    # Middle element calculation
    middle = l + (r - l) // 2
    # Identify the median of the first, middle, and last elements
    pivot_candidates = [(A[l], l), (A[middle], middle), (A[r], r)]
    # Sort the tuple list by the first element of the tuple (the values)
    pivot_candidates.sort(key=lambda x: x[0])
    # Return the index of the median value
    return pivot_candidates[1][1]


with open("/Users/yiningqu/Desktop/研究生/algorithm/Quicksort/Quicksort", "r") as file:
    array = [int(line.strip()) for line in file]
    
total_comparisons = QuickSort(array, 0, len(array) - 1)
print(total_comparisons)
