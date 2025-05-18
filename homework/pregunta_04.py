"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    import os


    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'files', 'input', 'data.csv')
    # Abre el archivo data.csv en modo lectura
    with open(file_path, 'r') as file:
        lines = file.readlines()

    meses = {}

    for line in lines:
        # La tabulacion es el separador de columnas
        columns = line.strip().split('\t')
        fecha = columns[2]
        mes = fecha.split('-')[1]

        # Incrementa el contador para el mes
        if mes in meses:
            meses[mes] += 1
        else:
            meses[mes] = 1

    # Convierte el diccionario a una lista de tuplas
    sorted_counts = sorted(meses.items())

    return sorted_counts


if __name__ == '__main__':
    print(pregunta_04())
