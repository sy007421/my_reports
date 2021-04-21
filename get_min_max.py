def get_min_max(L):
    if len(L) == 0:
        return (None, None)

    Maxs= Mins = L[0]
    for i in L:
        if i >= Maxs:
            Maxs = i
        elif i <= Mins:
            Mins = i
    return (Mins, Maxs)

arr = [7, 1, 3, 9, 5]

okc = get_min_max(arr)

print(okc)
    
