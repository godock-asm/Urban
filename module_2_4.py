
#Домашнее задание по теме "Цикл For"
#Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [ 2, 3, 5, 7, 11, 13]
print(*primes)
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
print(*not_primes)
for n in numbers:
    print(n)

    primes = []
    not_primes = []

    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
            else:
                not_primes.append(num)

    print(f'Primes: {primes}')
    print(f'Not Primes: {not_primes}')



#Домашнее задание по теме "Цикл While"
#Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [ 2, 3, 5, 7, 11, 13]
print(*primes)
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
print(*not_primes)


primes = []
not_primes = []
n=1
while numbers<=[15]:
        if numbers > [1]:
            is_prime = True
        range(2, 15)
while numbers < [16]:
            if numbers % n == 0:
                is_prime = False
            range(2, 16)
            break
if is_prime:
    primes.append(n)
else:
    not_primes.append(n)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')



