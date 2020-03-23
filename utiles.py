import sys
def open_txt_asociado():
    """Sirve para cargar txt con el mismo nombre que el archivo .py"""
    d = f'{sys.argv[0][:-2]}txt'
    with open(d, 'r') as f:
        return f.read()
