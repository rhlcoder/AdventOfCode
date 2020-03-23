from utiles import open_txt_asociado

lista = open_txt_asociado()
lineas = lista.splitlines()
strings = [l.split('x') for l in lineas]
dimensiones = [sorted(list(map(int, i))) for i in strings]


def area_papel(l: int, w: int, h: int) -> float:
    """paper needed: 2*l*w + 2*w*h + 2*h*l + smallest area
    
    Arguments:
        l {int} -- length
        w {int} -- width
        h {int} -- height
    
    Returns:
        float -- Area del papel
    """
    return 2 * l * w + 2 * w * h + 2 * h * l + l * w


def ribbon(l: int, w: int, h: int) -> int:
    """Ribbon needed to wrap a present: smallest perimeter + package volume
    
    Arguments:
        l {int} -- length
        w {int} -- width
        h {int} -- height
    
    Returns:
        int -- Largo de la cinta
    """
    return l * 2 + w * 2 + l * w * h


def sum_lista(func, lista: list) -> float:
    """Con el * expando la tupla BOOM!
    
    Arguments:
        func {function} -- La funcion que devuelve el calculo apropiado
        lista {List} -- La lista a calcular
    """
    return sum((func(*tupla) for tupla in lista))


total_paper = sum_lista(area_papel, dimensiones)
total_ribbon = sum_lista(ribbon, dimensiones)

print(f"Total paper needed: {total_paper}")
print(f"Total ribbon needed: {total_ribbon}")
