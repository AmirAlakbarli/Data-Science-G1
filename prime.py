number = int(input())


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            return False
    return True


def n_th_prime(n):
    if(n == 1):
        return 2
    elif(n == 2):
        return 3

    count = 3
    first_num = 5
    flag = 1
    while(count < n):
        if(is_prime(first_num)):
            count += 1

        if(flag):
            first_num += 2
            flag = 0
        else:
            first_num += 4
            flag = 1
    return first_num


print(n_th_prime(number))
