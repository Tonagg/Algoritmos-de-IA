def hanoi(n, origen='A', destino='C', auxiliar='B'):
    """
    Resuelve Torres de Hanoi para n discos.
    origen: poste de inicio
    destino: poste final
    auxiliar: poste de apoyo
    """
    if n == 1:
        print(f'  Mover disco 1: {origen} --> {destino}')
        return

    # Paso 1: mover n-1 discos al auxiliar
    hanoi(n - 1, origen, auxiliar, destino)

    # Paso 2: mover disco más grande al destino
    print(f'  Mover disco {n}: {origen} --> {destino}')

    # Paso 3: mover n-1 discos del auxiliar al destino
    hanoi(n - 1, auxiliar, destino, origen)

def hanoi_contador(n, origen='A', destino='C', auxiliar='B', cont=[0]):
    """Versión que cuenta movimientos"""
    if n == 1:
        cont[0] += 1
        print(f'  [{cont[0]}] Disco 1: {origen} --> {destino}')
        return
    hanoi_contador(n-1, origen, auxiliar, destino, cont)
    cont[0] += 1
    print(f'  [{cont[0]}] Disco {n}: {origen} --> {destino}')
    hanoi_contador(n-1, auxiliar, destino, origen, cont)
