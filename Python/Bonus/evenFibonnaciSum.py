

val = int(input("Enter value: "));



def iterativeSumEvenFibonacci(limit):
    # if limit <= 2:
        # return 0

    # sumOfEvens = 2
    sumOfEvens = 0
    first = 1
    second = 1
    current = first + second
    while current < limit:
        if current % 2 == 0:
            sumOfEvens+=current
        first = second
        second = current
        current = first + second
    return sumOfEvens




print(iterativeSumEvenFibonacci(val))