from utiles import open_txt_asociado

vectors = open_txt_asociado()
santa_vector = [vectors[i] for i in range(len(vectors)) if i % 2 == 0]
robot_santa_vector = [vectors[i] for i in range(len(vectors)) if i % 2 == 1]


def coord(vector, s):
    if vector == "^": s[0] += 1
    if vector == "v": s[0] -= 1
    if vector == ">": s[1] += 1
    if vector == "<": s[1] -= 1
    return s


# VERSION 3 (usando sets)
def count_moves(vectors):
    s = [0, 0]
    set_de_coordenadas = set()
    for i in vectors:
        coord(i, s)
        set_de_coordenadas.add(str(s))
    return set_de_coordenadas


solo_santa = count_moves(vectors)
union_de_santas = count_moves(robot_santa_vector).union(count_moves(santa_vector))

print(f"\nCantidad de casas visitadas al menos una vez:")
print(f"Santa solo: {len(solo_santa)} casas")
print(f"Santa + Robo-Santa: {len(union_de_santas)} casas")


# VERSION 2 (usando diccionarios)
# d = {str([0, 0]): 1}
#
#
# def count_moves(vectors, d):
#     s = [0, 0]
#     for i in vectors:
#         coord(i, s)
#         if str(s) in d.keys():
#             d[str(s)] += 1
#         else:
#             d[str(s)] = 1
#     return d
# print(f"Cantidad de casas visitadas al menos una vez: {len(count_moves(vectors, d))}")


# VERSION 1 (Usando listas y cochinadas -ilegible y mala perf-)
# s = [0, 0]
# acc = [[0, 0]]
# for i in santa_vector:
#     n = coord(i, s)
#     acc.append([n[0], n[1]])
# s = [0,0]
# for i in robot_santa_vector:
#     n = coord(i, s)
#     acc.append([n[0], n[1]])
# m = {str(i): acc.count(i) for i in acc}
# print(f'Cantidad de casas visitadas al menos una vez con la ayuda de Robo-Santa: {len(m)}')
# 
# d = {str([0, 0]): 1}
# s = [0, 0]
# for i in santa_vector:
#     n = coord(i, s)
#     if str(s) in d.keys():
#         d[str(s)] += 1
#     else:
#         d[str(s)] = 1
# s = [0, 0]
# for i in robot_santa_vector:
#     n = coord(i, s)
#     if str(s) in d.keys():
#         d[str(s)] += 1
#     else:
#         d[str(s)] = 1
# 
# print(
#     f"Cantidad de casas visitadas al menos una vez con la ayuda de Robo-Santa: {len(d)}"
# )
