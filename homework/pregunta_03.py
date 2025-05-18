"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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
        value = int(columns[1])

        # Suma el valor a la letra correspondiente
        if letter in letras:
            letras[letter] += value
        else:
            letras[letter] = value

    # Convierte el diccionario a una lista de tuplas
    sorted_sums = sorted(letras.items())

    return sorted_sums


if __name__ == '__main__':
    print(pregunta_03())
