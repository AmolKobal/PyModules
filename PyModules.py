
def Prime(n):
    lst = []
    for i in range(2, n):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            lst.append(i)

    return lst
