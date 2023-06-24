directions = input()
result = {'U': 0, 'D': 0, 'R': 0, 'L': 0}

for d in directions:
    # check if the d is already in the direction
    result[d] += 1


print(abs(result['U']-result['D']) + abs(result['R']-result['L']) == 0)
