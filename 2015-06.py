# turn on 0,0 through 1,3
# turn off 0,0 through 0,3
# toggle 3,0 through 3,3

# 0000
# 0000
# 1111
# 0000

# if o == 'on': 1
# if o == 'off': 0
# if o == 'toggle': coords[2] = (coords[2] + 1) % 2


from utiles import open_txt_asociado
import textwrap
import pprint


def intificar(lista):
    def lista_int(x):
        if x.isdecimal():
            return int(x)
        return x

    o, x1, y1, x2, y2 = map(lista_int, lista)
    return [o, x1, y1, x2, y2]


txt = open_txt_asociado()
fmt = txt.replace(" through ", ",").replace("turn ", "").replace(" ", ",")
fmt = fmt.splitlines()
fmt = [s.split(",") for s in fmt]
fmt = (intificar(s) for s in fmt)

print(list(fmt))


def grid(merge, n):
    m = ""
    for i in merge.values():
        m += str(i)

    m = textwrap.wrap(m, n)

    for i in m:
        print(i)
    print("\n")


def gen(n):
    for x in range(n):
        for y in range(n):
            yield f"{x},{y}"


def rango(a, b):
    for x in range(a[0], b[0] + 1):
        for y in range(a[1], b[1] + 1):
            yield f"{x},{y}"


# actualizo los datos
def actualizar(luces, orden):
    return {**luces, **orden}


# probando de usar un dict compr para no fabricar los yields

d = {f"{str(x)},{str(y)}": 8 for x in range(5) for y in range(5)}
print("prueba comprehension")
grid(d, 5)
pprint.pprint(d)


# valores de prueba
a = (2, 2)
b = (3, 3)
matriz = 5

luces = {str(i): 0 for i in rango(0, matriz)}
pprint.pprint(luces)

orden = {str(i): 1 for i in rango(a, b)}
grid(luces, matriz)


luces = actualizar(luces, orden)
grid(luces, matriz)

a = (0, 0)
b = (0, 3)

orden = {str(i): 1 for i in rango(a, b)}
luces = actualizar(luces, orden)
grid(luces, matriz)

a = (1, 0)
b = (1, 3)

orden = {str(i): 1 for i in rango(a, b)}
luces = actualizar(luces, orden)
grid(luces, matriz)

uno = 1
uno = 1 ^ +True
cero = 0 ^ +True
print(f"prueba de xor para hacer el toggle: {uno } {cero}")
