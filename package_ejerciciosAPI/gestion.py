def maximoPoblacion(_paises):  # paises es una lista, cuidado!!!
    max = 0
    elQueMas = {}
    for pais in _paises:  # pais es un diccionario. cuidado!!!
        if pais["population"] > max:
            elQueMas = pais
            max = elQueMas["population"]
    return elQueMas  # estructura de diccionario


def los10MasPoblados(_paises):
    masPoblados = []
    elPais = {}
    for i in range(10):
        elPais = maximoPoblacion(_paises)
        masPoblados.append(elPais)
        _paises.remove(elPais)  # se elimina el país con ese nombre
        # de la lista. oJO!!! el remove produce error si no encuentra
    return masPoblados
