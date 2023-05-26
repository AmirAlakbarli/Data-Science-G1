

a = int(input("Enter the smalest value: "))
b = int(input("Enter the largest value: "))

for i in range(a, b):
    for j in range(2, int(i**(0.5))+1):
        if i % j == 0:
            break
    else:
        print(i)
