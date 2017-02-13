
numbers = [int(i) for i in input().split()]
odds = 0
evens = 0
for number in numbers:
    if number < 0:
        spyAlert = True
    elif number == 0:
        continue
    else:
        spyAlert = False
    if number % 2:  # odd
        binNumber = "{0:b}".format(number)
        for bit in binNumber:
            if bit is '1':
                if spyAlert:
                    odds -= 1
                else:
                    odds += 1
    else:  # even
        binNumber = "{0:b}".format(number)
        for bit in binNumber:
            if bit is '0':
                if spyAlert:
                    evens -= 1
                else:
                    evens += 1
if odds > evens:
    print("odds win")
elif evens > odds:
    print("evens win")
else:
    print("tie")
