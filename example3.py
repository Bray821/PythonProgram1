def find_missing(sequence):
    add_num = []
    order = []
    counter = 1
    dictonary = {}
    for i in sequence:
        if counter>= len(sequence):
            pass
        num = sequence[counter]-i
        dictonary[num] = f"{sequence[counter]} {i}"
        for i in dictonary.keys():
            order.append(i)
        order.sort()
        sorted_order = order[-1]
        for i in dictonary[sorted_order]:
            if i.isnumeric():
                integer_number = int(i)
                add_num.append(integer_number)
        return dictonary[sorted_order]

print(find_missing([1, 3, 5, 9, 11 ]))