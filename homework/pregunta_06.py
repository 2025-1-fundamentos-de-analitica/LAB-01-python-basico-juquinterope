"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
        letra = columns[4]

        # Separa las claves y valores
        claves_valores = letra.split(',')
        for clave_valor in claves_valores:
            clave, valor = clave_valor.split(':')
            valor = int(valor)

            # Si la clave no esta en el diccionario, inicializa su lista
            if clave not in valores:
                valores[clave] = [valor, valor]
            else:
                # Actualiza el maximo y minimo
                valores[clave][0] = max(valores[clave][0], valor)
                valores[clave][1] = min(valores[clave][1], valor)

    # Convierte el diccionario a una lista de tuplas
    sorted_values = sorted([(k, v[1], v[0]) for k, v in valores.items()])

    return sorted_values


if __name__ == '__main__':
    print(pregunta_06())
