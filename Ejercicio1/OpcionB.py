def caminos(n,m):
    lista = {}
    tot = []

    def mover(a,b,act):
        if a<0 or a>=n or b<0 or b>=m:
            return
        if (a,b) in lista:
            return
        act.append((a,b))
        lista[(a,b)] = 1
        if a==n-1 and b==m-1:
            tot.append(act[:])
        else:
            mover(a, b+3, act)
            mover(a+2, b, act)
        act.pop()
        del lista[(a,b)]

    mover(0,0,[])
    return tot

res = caminos(5,7)

print("Total de caminos encontrados ", len(res))

numero = 1
for c in res:
    print("Camino", numero)
    for paso in c:
        print(paso)
    print()
    numero += 1
