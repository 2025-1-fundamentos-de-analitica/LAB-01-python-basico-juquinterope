"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    import os


    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'files', 'input', 'data.csv')
    # Abre el archivo data.csv en modo lectura
    with open(file_path, 'r') as file:
        lines = file.readlines()

    valores = {}

    for line in lines:
        # La tabulacion es el separador de columnas
        columns = line.strip().split('\t')
        letra = columns[0]
        valor = int(columns[1])

        # Si la letra no esta en el diccionario, inicializa su lista
        if letra not in valores:
            valores[letra] = [valor, valor]
        else:
            # Actualiza el maximo y minimo
            valores[letra][0] = max(valores[letra][0], valor)
            valores[letra][1] = min(valores[letra][1], valor)

    # Convierte el diccionario a una lista de tuplas
    sorted_values = sorted([(k, v[0], v[1]) for k, v in valores.items()])

    return sorted_values


if __name__ == '__main__':
    print(pregunta_05())
