def quickSort(array):
    if(len(array) <= 1):
        return array;
    else:
        pivot = array[0]
        higher = [i for i in array[1:] if i > pivot]
        lower = [i for i in array[1:] if i<= pivot]
        return quickSort(lower) + [pivot] + quickSort(higher)
        
    
print(quickSort([9,6,12,4,67]))