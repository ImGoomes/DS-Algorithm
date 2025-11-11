def countItems(list):
    if(len(list) == 0):
        return 0
    else:
        return 1 + countItems(list[1:])

print(countItems([1,3,4,5,9]))
