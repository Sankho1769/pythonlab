def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return result + left + right

values = list(map(int, input("Enter numbers: ").split()))
print("Sorted:", merge_sort(values))
