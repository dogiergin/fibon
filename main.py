def fibon(m):
    if ( m == 0 ):
        return 0
    elif( m == 1 ):
        return 1
    else:
        return fibon(m-1) + fibon(m-2)

g=int(input("istediğiniz fibonacci adımını giriniz : "))
print(fibon(g))
