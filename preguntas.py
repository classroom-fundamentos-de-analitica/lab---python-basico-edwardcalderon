"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from hashlib import new
import string
from operator import itemgetter
from itertools import groupby

csv_file = csv.reader(open("data.csv", encoding="utf-8"),
                      delimiter="\t", quotechar='"')


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    dist = 0
    for row in csv_file:
        _dist = row[1]
        try:
            _dist = int(_dist)
        except ValueError:
            _dist = 0

        dist += _dist
    """ print(dist) """
    return dist


""" pregunta_01() """


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letters_list = []
    column = []
    for row in csv_file:
        _dist = row[0]
        column.append(_dist)
        if len(letters_list) == 0 or _dist not in letters_list:
            letters_list.append(_dist)

    letters_list.sort()
    count = []
    for letter in letters_list:
        occurrences = column.count(letter)
        count.append(occurrences)

    res = []
    for i in range(len(letters_list)):
        tupple_rta = letters_list[i], count[i]
        res.append(tupple_rta)

    return res


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letters_list = []
    column = []
    res = []
    for row in csv_file:
        _dist = row[0]
        _value = row[1]
        if len(letters_list) == 0 or _dist not in letters_list:
            letters_list.append(_dist)
            column.append(_value)
            index = letters_list.index(_dist)
            tupple_rta = letters_list[index], column[index]
            res.append(tupple_rta)
            continue
        if _dist in letters_list:
            index = letters_list.index(_dist)
            tupple_rta = letters_list[index], column[index]
            res.remove(tupple_rta)
            column[index] = int(column[index]) + int(_value)
            tupple_rta = letters_list[index], column[index]
            res.append(tupple_rta)

    res.sort()
    """ for items in res:
        print(items) """
        
    return res

def reducer_small_data(sequence):
    contador = {}
    for key, value in sequence:
        contador[key] = contador.get(key, 0) + value
    return list(contador.items())

def shuffle_and_sort(sequence):
    f = itemgetter(0)
    sequence = sorted(sequence, key=f)
    return sequence
   
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    column = []
    for row in csv_file:
        _value = row[2]
        splited_value = _value.split("-")
        column.append((splited_value[1],1))

    res = reducer_small_data(column)

    return shuffle_and_sort(res)

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    grouped_max_min_list = []
    for key, group in groupby(sorted(csv_file, key=lambda x: x[0]), key=lambda x: x[0]):
        max_elm = float("-inf")
        min_elm = float("inf")
        for string_elm in group:
            num_elm = int(string_elm[1])
            if num_elm > max_elm:
                max_elm = num_elm
            if num_elm < min_elm:
                min_elm = num_elm
        grouped_max_min_list.append((key, max_elm, min_elm))
    return grouped_max_min_list

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    grouped_max_min_list = []
    for key, group in groupby(sorted(csv_file, key=lambda x: x[4]), key=lambda x: x[4]):
        for string_elm in group:
            elm = string_elm[4].split(',')
            max_elm = float("-inf")
            min_elm = float("inf")
            for _elm in elm:
                el_ = _elm.split(':')
                num_elm = int(el_[1])
                if num_elm > max_elm:
                    max_elm = num_elm
                if num_elm < min_elm:
                    min_elm = num_elm
                grouped_max_min_list.append((el_[0], max_elm, min_elm))
    return grouped_max_min_list

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    grouped_max_min_list = []
    for key, group in groupby(sorted(csv_file, key=lambda x: x[1]), key=lambda x: x[1]):
        letters = []
        for string_elm in group:
            letters.append(string_elm[0])
        grouped_max_min_list.append((key, letters))
    return grouped_max_min_list

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    grouped_max_min_list = []
    for key, group in groupby(sorted(csv_file, key=lambda x: x[1]), key=lambda x: x[1]):
        letters = []
        for string_elm in group:
            if(string_elm[0] not in letters):
                letters.append(string_elm[0])
        letters.sort()        
        grouped_max_min_list.append((key, letters))
    return grouped_max_min_list

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    grouped_dict = {}
    for key, group in groupby(sorted(csv_file, key=lambda x: x[4]), key=lambda x: x[4]):
        elements = key.split(',')
        print(elements)
        for el in elements:
            key = el.split(":")[0]
            if(key not in grouped_dict ):
                print(key)
                grouped_dict.update({key: 0})
            if(key in grouped_dict):
                new_val = grouped_dict.get(key) + 1
                grouped_dict.update({key: new_val})
    sorted_list = sorted(grouped_dict.items())
    d = dict((sorted_list[i]) for i in range(len(sorted_list)))
    return d

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
