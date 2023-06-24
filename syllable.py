word = input()

qalin_saitler = ['a', 'ı', 'o', 'u']
ince_saitler = ['e', 'i', 'ö', 'ü']

qalin_say = 0
ince_say = 0

for i in word:
    if i in qalin_saitler:
        qalin_say += 1
    elif i in ince_saitler:
        ince_say += 1

print(not(qalin_say and ince_say))
