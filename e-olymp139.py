numbers = list(map(int, input().split()))

A, B, C, D, N, K = numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]
max = 0
for i in range(0, K):
    for x in range(int(N/A) + 1):
        y = int((N-A*x)/B)
        if(C*x+D*y >= max):
            max = C*x+D*y
    N += max

print(N)
