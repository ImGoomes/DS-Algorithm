target = 9
elements = [11, 15, 2, 7]
position = []

for i in range(len(elements)):
    if(elements[i] <= target):
        target -= elements[i]
        position.append(i)
        continue

print(position)

