import re
from utiles import open_txt_asociado

txt = open_txt_asociado()
texto = txt.splitlines()

#VERSION 2
def check_niceness(text):
    check_substr = re.subn(r"ab|cd|pq|xy", '', text)[1] == 0
    check_repeated = re.subn(r"(\w)\1", "", text)[1] >= 1
    check_vowels = re.subn(r'[aeiou]', '', text)[1] >= 3

    if not check_substr:
        return 0
    if not check_repeated:
        return 0
    if not check_vowels:
        return 0
    return 1


def new_check_niceness(text):
    check_AAxAA = re.subn(r"(\w\w)\w*?\1", "", text)[1]
    check_BxB = re.subn(r"(\w)\w\1", "", text)[1]

    if not check_AAxAA:
        return 0
    if not check_BxB :
        return 0
    return 1


nice_guys = sum(check_niceness(t) for t in texto)
new_nice_guys = sum(new_check_niceness(t) for t in texto)

print(f"Number of nice guys: {nice_guys}")
print(f"New number of nice guys: {new_nice_guys}")


# VERSION 1
# def check_niceness(text):
#     check_substr = [text.find(x) for x in ("ab", "cd", "pq", "xy")] == [-1, -1, -1, -1]
#     check_repeated = (
#         len([text[i] for i in range(len(text) - 1) if text[i] == text[i + 1]]) > 0
#     )
#     check_vowels = len([x for x in text if x in ("aeiou")]) >= 3

#     if not check_substr:
#         return 0
#     if not check_repeated:
#         return 0
#     if not check_vowels:
#         return 0
#     return 1
#
#
# def new_check_niceness(text):
#     aaxaa = re.compile(r"(\w\w)\w*?\1")  #  aa---aa
#     bxb = re.compile(r"(\w)\w\1")  #  bxb
#
#     if not re.subn(aaxaa, "", text)[1]:
#         return 0
#     if not re.subn(bxb, "", text)[1]:
#         return 0
#     return 1
