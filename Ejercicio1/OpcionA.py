def revisar(n,m):
    vis = []

    def checar(x,y):
        if x<0 or x>=n or y<0 or y>=m:
            return False
        if (x,y) in vis:
            return False
        if x==n-1 and y==m-1:
            return True
        vis.append((x,y))
        r1 = checar(x, y+3)
        r2 = checar(x+2, y)
        if r1 or r2:
            return True
        vis.remove((x,y))
        return False

    return checar(0,0)

resultado = revisar(5,7)

if resultado:
    print("Si existe al menos un camino del inicio al final :)")
else:
    print("No existe ningún camino posible :(")
