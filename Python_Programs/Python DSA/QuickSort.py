def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    return quick_sort([x for x in a if x < pivot]) + [x for x in a if x == pivot] + quick_sort([x for x in a if x > pivot])

values = list(map(int, input("Enter numbers: ").split()))
print("Sorted:", quick_sort(values))
