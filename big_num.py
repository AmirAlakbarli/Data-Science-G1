# take numbers from console in one line

# input: 1 2 3 4 5 6 7 8 9 10

numbers = input().split(" ")
numbers = [int(i) for i in numbers]


for i in range(len(numbers)):
    if(i == len(numbers)-1):
        if((numbers[i] > numbers[i-1]) and (numbers[i] > numbers[0])):
            print(numbers[i])

    else:
        if((numbers[i] > numbers[i-1]) and (numbers[i] > numbers[i+1])):
            print(numbers[i])

