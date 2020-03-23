import hashlib

key = "iwrupvqb"


def find_zero_prefixed_hash(key, zeros):
    i = 1
    while True:
        clave = f"{key}{i}"
        h = hashlib.md5(clave.encode("utf-8"))
        if (h.hexdigest()[:zeros]) == "0" * zeros:
            return [i, h.hexdigest()]
        i += 1


five = find_zero_prefixed_hash(key, 5)
six = find_zero_prefixed_hash(key, 6)

print(f"Encontrado el numero {five[0]} que corresponde al hash {five[1]}")
print(f"Encontrado el numero {six[0]} que corresponde al hash {six[1]}")
