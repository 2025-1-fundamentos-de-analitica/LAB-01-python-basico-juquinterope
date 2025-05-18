"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]

    """
    import os


    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'files', 'input', 'data.csv')
    # Abre el archivo data.csv en modo lectura
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Lista para almacenar las tuplas
    resultado = []
    
    for line in lines:
        # Divide la línea por tabulaciones
        columns = line.strip().split('\t')
        
        # Obtiene la letra de la columna 1
        letra = columns[0]
        
        # Cuenta elementos en columnas 4 y 5
        elementos_col4 = len(columns[3].split(','))
        elementos_col5 = len(columns[4].split(','))
        
        # Crea la tupla y la anade al resultado
        resultado.append((letra, elementos_col4, elementos_col5))
    
    return resultado


if __name__ == '__main__':
    print(pregunta_10())
