"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}

    """
    import os


    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'files', 'input', 'data.csv')
    # Abre el archivo data.csv en modo lectura
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    sumas = {}

    for line in lines:
        # Divide la línea por tabulaciones
        columns = line.strip().split('\t')
        
        # Obtiene el valor de la columna 2
        valor = int(columns[1])
        
        # Obtiene las letras de la columna 4
        letras = columns[3].split(',')
        
        # Suma el valor para cada letra
        for letra in letras:
            sumas[letra] = sumas.get(letra, 0) + valor

    # Ordena el diccionario por clave
    return dict(sorted(sumas.items()))


if __name__ == '__main__':
    print(pregunta_11())
