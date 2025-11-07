def soma(lista):
    if(len(lista) == 0):
        return 0
    else:
        return lista[0] + soma(lista[1:])

print(soma([2,4,6]))
