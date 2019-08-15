def find_max_prod(number, n):
    """ 
    Find the maximum product of n adjacent digits in a 1000 digit number
        Parameters:
            number - 1000 digit number to use
            n - the nth number of adjacent digits
        Returns:
            max_prod - the maximum product of all nth adjecent digits
    """
    digits =[int(x) for x in str(number)] #break into digits
    max_prod = 0
    for x in range(len(digits)):
        if x+n < len(digits):
            prod = np.prod(digits[x:x+n])
        else:
            prod = np.prod(digits[-n])
        
        if prod > max_prod: max_prod = prod
    return max_prod
