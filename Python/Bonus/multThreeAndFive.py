val = int(input("Enter value: "))


def giveSumsThreeAndFiveIteratively(limit):
    upperLimit = limit
    # print(limit)
    # print(upperLimit)
    if upperLimit < 0:
        upperLimit = upperLimit * -1

    sum = 0


    for i in range(0, upperLimit):
        # if i % 3 == 0 and i% 5 == 0:
        #     sum+=i
        # elif i %3 == 0:
        #     sum+=i
        # elif i % 5 == 0:
        #     sum+=i
        if i % 3 == 0 or i % 5 == 0:
            sum+=i

    if limit < 0:
        return sum*-1
    else:
        return sum




print(giveSumsThreeAndFiveIteratively(val))
