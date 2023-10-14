def merge_sort(list):
    """
    sorts a list in ascending order
    returns a new sorted list 
    
    divide: find the midpoint of the list and divide it into sublists
    conquer: recursively sort the sublists into the previous setup
    combine: Merge the sorted sublists created in the previous setup
    """
    if len(list)<=1:
        return list
    
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)
def merge(left,right):
    """
    Merges two lists sorting them in the process
    Returns a new merged list
    """
    L = [] ; i = 0 ; j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            L.append(left[i])
            i += 1
        else:
            L.append(right[j])
            j += 1
    while i < len(left):
        L.append(left[i])
        i += 1
    while j<len(right):
        L.append(right[j])
        j += 1
    return L
def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0]<list[1] and verify_sorted(list[1:])
list = [23,42,12,32,43,5,2,123,9]
print(list)
print(merge_sort(list),verify_sorted(merge_sort(list)))