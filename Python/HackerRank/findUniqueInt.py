

def returnUniqueInt(arr):
    if len(arr) < 1:
        return None
    IntCount = {}

    for x in arr:
        if x in IntCount:
            IntCount[x] = IntCount[x] + 1
        else:
            IntCount[x] = 1
    for y in arr:
        if IntCount[y] == 1:
            return y
    return None


example = [3, 4, 4, 2, 3, 9, 2, 9]

print(returnUniqueInt(example))