def evenOdd(list):
    evens = []
    odds = []
    for item in list:
        if len(item)%2 == 0:
            evens.append(item)
        else:
            odds.append(item)

    for x in range(len(evens)):
        evens[x] = evens[x].replace(evens[x][0], 'b', 1)

    for x in range(len(odds)):
        odds[x] = odds[x][:-1] + 'c'

    for x in range(len(evens)):
        print(evens[x])

    for x in range(len(odds)):
        print(odds[x])

    even_list = evens
    return even_list

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
even_list = evenOdd(names_list)

for x in range(len(even_list)):
    print (even_list[x])
            
