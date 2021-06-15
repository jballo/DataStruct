numA = 3
numB = 8
numC = 10


def bruteForcereturnSmallestPrime(numGiven):
    highestPrime = numGiven
    lowestPrimeFound = False
    while not lowestPrimeFound:
        highestPrime += 1
        numA = 2
        numB = 2
        for x in range (1, highestPrime):
            for y in range (1, highestPrime):
                if (x * y) == highestPrime:
                    numA = x
                    numB = y

        if (numA * numB) != highestPrime:
            lowestPrimeFound = True

    return highestPrime

def slightlyEfficientNextSmallestPrime(numGiven):
    lowestPrime = numGiven+1
    lowestPrimeFound = False
    while not lowestPrimeFound:
        divisibles = 0
        for x in range (2, lowestPrime):
            if lowestPrime % x == 0:
                divisibles+=1
        if divisibles == 0:
            lowestPrimeFound = True
        else:
            lowestPrime+=1
    return lowestPrime
            


print(slightlyEfficientNextSmallestPrime(numA))
print(slightlyEfficientNextSmallestPrime(numB))
print(slightlyEfficientNextSmallestPrime(numC))    
print(slightlyEfficientNextSmallestPrime(0)) 
print(slightlyEfficientNextSmallestPrime(1)) 
print(slightlyEfficientNextSmallestPrime(2)) 
print(slightlyEfficientNextSmallestPrime(3))
print(slightlyEfficientNextSmallestPrime(4))
