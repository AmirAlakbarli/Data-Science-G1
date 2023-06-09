import math

# first way


def seperate(n):
    res = ""
    while n > 0:
        res = str(n % 10) + " " + res
        n = n//10
    return res

# num = int(input())
# print(seperate(num))

# second way


    def seperate1(num):

        num_of_dig = int(math.log10(num))

        for i in range(num_of_dig, -1, -1):
            dec = 10**i
            digit = (num//dec) % 10
            print(digit, end=' ')


    num = int(input())
    seperate1(num)
