List2 = [12,14,-95,3]
for i in range(0):
    value = int(input())
    List2.append(value)

# finding all positive number from the list
posNoList = list(filter(lambda i: (i >= 0), List2))

# printing all positive values of the list
print(posNoList)
