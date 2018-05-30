def findsum(numrange):
    """
    Finds and returns the sum of all numbers divisble by 3 or 5 below parameter numrange.
        Parameters:
            numrange - Must be a natural number. No floats.
        Returns:
            multisum - sum of all numbers from 1 to below numrange that are divisble by 3 or 5
    """
    multisum = 0
    for i in range(numrange):
        num = i + 1 #steps over zero-index
        if num >= numrange: #Checks to see if we have hit upper boundary of numrange
            break
        elif num % 3 == 0 or num % 5 == 0: #Checks if divisble by 3 or 5
            multisum += num #Adds num divisble by 3 or 5
    return multisum

n = 1000 #input value for problem
totalsum = findsum(n)
print('The sum of numbers divisble by 3 or 5 below {} is {}'.format(n, totalsum))
