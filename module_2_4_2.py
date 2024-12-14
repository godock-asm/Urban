from module_2_4 import is_prime
#Домашнее задание по теме "Цикл While"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [ 2, 3, 5, 7, 11, 13]
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]

primes = []
not_primes = []

while numbers < [16] :
    num = numbers.pop
    print(f'Numbers: {num}')
    if num > 1:
        is_prime = True
        for i in range(2, [num]):
            if [num] % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')