# first element as pivot

def QuickSort(A, l, r):
    # If the array contains only one element, return immediately
    if l >= r:
        return 0  # No comparisons are done for a single element

    # ChoosePivot is simply the first element for this version
    p = ChoosePivot(A, l, r)

    # Partition around the pivot and get the new pivot index
    comparisons = r - l  # since we will compare each element with the pivot
    p_index = Partition(A, l, r, p)

    # Recursively sort the first part
    comparisons += QuickSort(A, l, p_index - 1)

    # Recursively sort the second part
    comparisons += QuickSort(A, p_index + 1, r)

    return comparisons

def ChoosePivot(A, l, r):
    # For this version of QuickSort, we always choose the first element as the pivot
    return A[l]

def Partition(A, l, r, p):
    # The partition subroutine as per the provided pseudocode
    A[l], A[A.index(p)] = A[A.index(p)], A[l]  # Move the pivot to the start if it's not already there
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    # Swap the pivot into its correct place
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

with open("/Users/yiningqu/Desktop/研究生/algorithm/Quicksort/Quicksort", "r") as file:
    array = [int(line.strip()) for line in file]
    
total_comparisons = QuickSort(array, 0, len(array) - 1)
print(total_comparisons)