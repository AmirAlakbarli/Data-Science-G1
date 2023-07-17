nominals = [10, 20, 50, 100, 200, 500]
n = int(input())
res_count = 0

for i in nominals[::-1]:
    count = int(n/i)
    res_count += count
    n -= count * i

if(n != 0):
    print(-1)
else:
    print(res_count)
