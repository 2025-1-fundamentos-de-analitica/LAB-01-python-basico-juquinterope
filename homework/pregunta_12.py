"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

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
        
        # Obtiene la letra de la columna 1
        clave = columns[0]
        
        # Procesa los elementos de la columna 5
        elementos = columns[4].split(',')
        
        # Suma los valores numéricos de cada elemento
        suma_valores = sum(int(elemento.split(':')[1]) for elemento in elementos)
        
        # Acumula la suma para cada clave
        sumas[clave] = sumas.get(clave, 0) + suma_valores

    return dict(sorted(sumas.items()))


if __name__ == '__main__':
    print(pregunta_12())
