N = int(input())

sum = 0
i = 0
for i in range(N, 0, -1):
    sum += 1/i
    if(sum > 0.5):
        break

print(i)
