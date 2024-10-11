def find_slot_with_increment(my_map, key, hash_value, delta):
    """
    Busca una key y retorna su posición (si la encuentra).
    Si No se encuentra debe retornar la primer posición disponible.

    Utiliza los valores hash_value y delta para definir las posiciones de busqueda.
    Si la posición esta ocupada o fue borrada, busca la próxima posición disponible aumentando delta al valor anterior.

    :param my_map: la tabla de hash a examinar
    :type my_map: map_probing_delta
    :param key: Llave a buscar
    :type key: any
    :param hash_value: Posición inicial en la tabla de hash para la busqueda
    :type hash_value: int
    :param delta: valor de incremento en la búsqueda si la posición de busqueda esta ocupada o fue borrada.
    :type delta: int

    :return: Retorna una tupla con dos valores.
             El primero indica si se encontro o no la llave (True o False).
             El segundo la posición en la tabla de hash donde se encuentra la llave o 
             la primer posición disponible para agregarla.
    :rtype: bool, int
    """
    elements = my_map['table']['elements']
    i = False
    while i == False:
        if (elements[hash_value]['key'] == '_EMPTY_') or (elements[hash_value]['key'] != key and elements[hash_value]['key'] != None):
            elements[hash_value] += delta
            i = False
        else:
            i = True

    if elements[hash_value]['key'] == key:
        return True, hash_value
    elif elements[hash_value]['key'] == None:
        return False, hash_value
    
    
    
            

