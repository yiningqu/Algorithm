def merge_and_count_inversions(left, right):
    outputarr = []
    count = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            outputarr.append(left[i])
            i += 1
        else:
            outputarr.append(right[j])
            j += 1
            count += len(left) - i  # Count inversions here

    # Add any remaining items from the arrays
    outputarr += left[i:]
    outputarr += right[j:]

    return outputarr, count

def sort_and_count(array):
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    left, left_count = sort_and_count(array[:mid])
    right, right_count = sort_and_count(array[mid:])
    merged, merge_count = merge_and_count_inversions(left, right)

    return merged, left_count + right_count + merge_count

# Use this to read in the integer array and count inversions
with open("/Users/yiningqu/Desktop/研究生/algorithm/HW2/IntegerArray.txt", "r") as file:
    intarr = [int(line.strip()) for line in file]

# Sort array and count inversions
sortedarr, count = sort_and_count(intarr)

# Output the count and the first few elements of the sorted array
print("Number of inversions:", count)
