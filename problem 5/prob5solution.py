from collections import Counter
from collections import defaultdict
import numpy as np

def find_factors(num):
    #Returns a list of prime factors for number passed
    factors = []
    i = 2
    while num >= 2:
        if num % i == 0:
            factors.append(i)
            num = num/i
        else:
            i += 1
    return factors

def find_lcm_of_range(min_range, max_range):
    #Returns LCM of numbers ranging from min_range to max_range
    #Parameters:
    #           min_range - starting point of range (int)
    #           max_range - end point of range. Use desired end point as function accounts for zero index (int)
    count = defaultdict(int)
    for number in range(min_range, max_range+1):
        factor_count = dict(Counter(find_factors(number))) #Outputs dict number of occurences of each factor
        for k in factor_count: #find the greatest occurence of each factor of all numbers in range
            if count[k] < factor_count[k]:
                count[k] = factor_count[k]
    return np.prod([k**v for k,v in count.items()])
