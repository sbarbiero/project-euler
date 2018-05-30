def findfibsum(fiblimit):
    """
    Finds even numbers between 1 and 4 million in the fibonacci sequence and returns the sum of those numbers
        Parameters:
            fiblimit - establish upper boundary of fibonacci terms to calculate
        Returns:
            fibsum - sum of even numbers in the fibonacci sequence from 1 to fiblimit
    """
    fibsum = 0
    term1, term2 = 1,2 #start fibonacci sequence here
    while term2 <= fiblimit:
        if term2 % 2 == 0:
            fibsum += term2
        term1, term2 = term2, term1 + term2
    return fibsum

limit = 4000000 #4 MILLION
evensum = findfibsum(limit)
print('The sum of even numbers in the fibonacci sequence from 1 to {} is {}.'.format(limit, evensum))
