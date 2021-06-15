
stringA = 'person'
stringB = 'soner'
stringC = 'pot'


def substringCheck(stringOne, stringTwo):
    S = set()
    for x in stringOne:
        S.add(x)

    for y in stringTwo:
        if not y in S:
            return False
    return True


print(substringCheck(stringA, stringB))
print(substringCheck(stringA, stringC))
