"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def Prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return(0)
    return(1)

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError('input is not positive')
    i = 2
    while(1):
        if(Prime(i)):
            list.append(i)
            if(len(list)==number_of_primes):
                break
        i+=1
    return list
