import math
#import matplotlib.pyplot as plt

def primeList(n, theta):
    primes = [2]
    boolean = True
    for i in range(3, n):
        boolean = True
        #print("i=" + str(i))
        while boolean:
            for d in primes:
                #print("d=" + str(d))
                z = i % d
                x = math.floor(d * theta) % d
                if z != x:
                    #print(str(i) + " is prime to modulus " + str(d))
                    continue
                else:
                    #print(str(i) + " is a multiple of " + str(d))
                    boolean = False  # i is composite
                    break
            if boolean:
                primes.append(i)
                #print("adding " + str(i) + " to primes")
                boolean = False
                break
    return primes

print(primeList(100,0))
