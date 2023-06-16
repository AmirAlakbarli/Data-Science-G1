
# #! problem1 solution 1
# print(int(input()) % 10)

# #! problem 1 solution 2
# number = input()
# print(number[-1])


# ! problem 3 solution

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


count = 2
mirror_count = [2, 3]
prime = 5
isOdd = 0
while(count < 10):
    if is_prime(prime) and is_prime(int(str(prime)[::-1])):
        mirror_count.append(prime)
        count += 1
    if (isOdd % 2 == 0):
        prime += 2
        isOdd = 1
    else:
        prime += 4
        isOdd = 0

print(mirror_count)

# ! problem 5 solution

qiymetler = [("Gunay", 95), ("Zehra", 100), ("Teymur", 45),
             ("Aysel", 49), ("Gulxende", 34)]

result = [i for i in qiymetler if i[1] >= 50]


#! problem 7 solution 1
a = [5, 20, 30, 60, 50]
filtered_a = list(filter(lambda x: x > 20, a))
mapped_a = list(map(lambda x: x**2, filtered_a))
print(mapped_a)
