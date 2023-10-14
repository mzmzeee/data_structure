def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint= (len(list))//2
        if list[midpoint]==target:
            return True
        else:
            if list[midpoint]<target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint],target)
            
def verify(result):
    print("target have been found",result)

numbers = [i for i in range(1,41)]
numbers.sort()
verify(recursive_binary_search(numbers,20))