
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True   
    for x in range(2, num):
        if num % x == 0:
            return False
    
    return True


print(is_prime(-1))
print(is_prime(2))
print(is_prime(11))
print(is_prime(19))
print(is_prime(29))
print(is_prime(25))
print(is_prime(61))

# Alternative Solution

def is_prime_number(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5 ):
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime_number(-1))
print(is_prime_number(2))
print(is_prime_number(11))
print(is_prime_number(19))
print(is_prime_number(29))
print(is_prime_number(25))
print(is_prime_number(61))