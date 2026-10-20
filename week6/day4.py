# Merge two ALREADY SORTED lists into one sorted list (O(n + m))
def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


# Split, sort each half (recursion), merge. Time O(n log n), space O(n).
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


if __name__ == "__main__":
    print(merge([1, 4, 7], [2, 3, 9]))
    print(merge([], [1, 2]))
    print(merge_sort([5, 2, 4, 1]))
    print(merge_sort([3, 1, 2]))
    print(merge_sort([]))
    print(merge_sort([7]))
    print(merge_sort([3, 1, 3, 2, 1]))
    print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
    print(merge_sort([5, 2, 4, 1]) == sorted([5, 2, 4, 1]))