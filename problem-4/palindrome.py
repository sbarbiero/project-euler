numbers = [x for x in range(100,1000)] #Create list of all 3 digit natural numbers
maxprod = 0
#find the product of every element by every element in list numbers
#i.e. 100 * 100, 100 * 101, 100 * 102, etc
for x in numbers:
    for y in numbers:
        pal = x * y #set product to palindrome test variable
        if str(pal) == str(pal)[::-1]: #test if product is palindrome
            if pal > maxprod: #check if palindrome product is greater than previous palindrome
                maxprod = pal
                
print('The largest product of two 3 digit numbers is {}.'.format(maxprod))
