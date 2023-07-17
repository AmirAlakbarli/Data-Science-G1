n = int(input())

list_ = list(range(1, n+1))

map_ = map(lambda x: str(x**2) + ", ", list_)

# remove last comma from map_
map_ = list(map_)
map_[-1] = map_[-1][:-2]

print("".join(map_))
