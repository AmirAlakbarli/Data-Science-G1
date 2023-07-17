n = int(input())

n_bin = bin(n)
count = 0
for i in n_bin:
    if i == '1':
        count += 1
print(count)
