# -*- encoding: utf-8 -*-
# Author(s): Abdelhalim Kadi <kadi.halim@gmail.com>
#Compute the prime factors of a given natural number.

def get_prime_factors(number):
    u"""
    Return prime factor list for a given number
        number - an integer number
        Example: get_prime_factors(8) --> [2, 2, 2].
    """
    if number == 1:
        return []

    #We have to begin with 2 instead of 1 or 0
    #to avoid the calls infinite or the division by 0
    for i in xrange(2, number):
        #Get remainder and quotient
        rd, qt = divmod(number, i)
        if qt == 0:
            return [i] + get_prime_factors(rd)

    return [number]
