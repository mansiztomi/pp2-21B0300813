def prime(num):
    if num <= 0:
        return "Not defined"
    elif num == 1:
        return "Not prime"
    for i in range(2, num):
        if num % i == 0:
            return "not prime"
    return "prime"


def filter_prime(list):
    prime_list = []
    for i in list:
        x = prime(i)
        if x == "prime":
            prime_list.append(i)
    return prime_list


print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 23, 24, 19, 100]))
