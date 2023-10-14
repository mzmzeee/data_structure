def binary_search(list , target):
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]< target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None
def verify(index):
    if index is not None:
        print(""" target found at index: """,index)
    else:
        print("not found")

numbers = [i for i in range(0,10)]
print()
numbers.sort()
verify(binary_search(numbers,9))
print()