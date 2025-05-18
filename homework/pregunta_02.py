"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    import os


    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'files', 'input', 'data.csv')
    # Abre el archivo data.csv en modo lectura
    with open(file_path, 'r') as file:
        lines = file.readlines()

    letras = {}

    for line in lines:
        # La tabulacion es el separador de columnas
        columns = line.strip().split('\t')
        letter = columns[0]

        # Incrementa el contador para la letra
        if letter in letras:
            letras[letter] += 1
        else:
            letras[letter] = 1

    # Convierte el diccionario a una lista de tuplas
    sorted_counts = sorted(letras.items())

    return sorted_counts


if __name__ == '__main__':
    print(pregunta_02())