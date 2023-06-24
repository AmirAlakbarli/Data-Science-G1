ip_address = input()

octets = ip_address.split('.')

# check if the length of octets is 4

if len(octets) != 4:
    print(False)

else:

    print(ip_address)

    # check if all elements of ip_address are bigger than 0 and less than 255

    for o in octets:
        if int(o) < 0 or int(o) > 255:
            print(False)
            break
    else:
        print(True)
