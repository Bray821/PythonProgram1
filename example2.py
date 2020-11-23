def find_outlier(integers):
    even_tab = []
    odd_tab = []
    even_counter = 0
    odd_counter = 0
    for i in integers:
        if i%2 == 0:
            even_tab.append(i)
            even_counter += 1
        else:
            odd_tab.append(i)
            odd_counter += 1
    
    if even_counter> odd_counter:
        return odd_tab[0]
    else:
        return even_tab[0]
