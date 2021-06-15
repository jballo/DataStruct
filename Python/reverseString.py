

stringA = 'hello'


def reverseString(givenString):
    backwards = ''
    for i in range(len(givenString)-1, -1, -1):
        backwards+=givenString[i]
    return backwards


print(reverseString(stringA))

print(reverseString('why hello there'))