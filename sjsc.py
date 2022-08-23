def csj(n):
    import names
    import random
    q = []
    for i in range(n):       
        a = names.get_full_name()
        b = random.randint(49,100)
        c = a + '.' + str(b)
        q.append(c)
    
    return q

