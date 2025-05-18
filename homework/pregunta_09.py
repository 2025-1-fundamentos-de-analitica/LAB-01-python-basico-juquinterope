"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    import os


    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'files', 'input', 'data.csv')
    # Abre el archivo data.csv en modo lectura
    with open(file_path, 'r') as file:
        lines = file.readlines()

    valores = {}
    for line in lines:
        # Divide la línea por tabulaciones
        columns = line.strip().split('\t')
        # Obtiene la columna 5 (índice 4) y divide por comas
        elementos = columns[4].split(',')
        
        # Para cada elemento en la columna 5
        for elemento in elementos:
            # Extrae solo la clave (parte antes del ':')
            clave = elemento.split(':')[0]
            # Incrementa el contador para la clave
            valores[clave] = valores.get(clave, 0) + 1
            
    return dict(sorted(valores.items()))


if __name__ == '__main__':
    print(pregunta_09())
