# 1 Вариант: без переменной-флага is_prime
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:  # перебор списка numbers
    counts = 0  # количество делений без остатка
    for j in range(1, i+1):  # перебор количества делителей без остатка
        if i % j == 0:
            counts += 1
        elif counts > 2:  # остановка перебора делителей без остатка если их больше двух
            break
    if counts == 2:  # проверка на количество делителей без остатка
        primes.append(i)
    elif counts > 2:
        not_primes.append(i)
print(primes)
print(not_primes)


# 2 Вариант: с переменной-флагом is_prime

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 1

for i in numbers:  # перебор списка numbers
    for j in range(2, i):  # перебор делителей от 2 до значения числа (невключительно) на наличие остатка при делении
        if i % j == 0:
            is_prime = False
            break # остановка перебора делителей без остатка если выявлен хотябы один
        else:
            is_prime = True

    if is_prime == True and i != 1:  # проверка на количество делителей без остатка
        primes.append(i)
    elif is_prime == False and i != 1:
        not_primes.append(i)
print(primes)
print(not_primes)
