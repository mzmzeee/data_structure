def liner_search(list ,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None 
def verify(index):
    if index is not None:
        print(""" target found at index: """,index)
    else:
        print("not found")

numbers = [i for i in range(0,10)]
print()
numbers.sort()
verify(liner_search(numbers,9))
print()