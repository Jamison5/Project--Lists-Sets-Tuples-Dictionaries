def remove_item(item: object, container: object, multi: bool=True) -> object:
    '''
    Next, you are going to implement the remove_item function that removes an item from any basic Python container (list, set, tuple, dict). The function has the following 
    parameters:

    item: The object to be removed from the container.

    container: The container from which the item is removed (list, set, tuple, dict).

    multi: The bool specifier indicating if only the first occurrence of the item should be removed (False) or all of them (True). This parameter has a default value set to 
    True.

    The function returns the updated container (or its copy if necessary).

    This is how the remove_item function handles removing an item from the individual container types:

    List: All the objects in the list that are equal to the item are removed from the list. In case, the multi argument is set to False only the first occurrence is removed.
    For example:

    container = [1, 2, 3, 4, 1]
    container = remove_item(1, container, False)
    container is now [2, 3, 4, 1]

    container = [1, 2, 3, 4, 1]
    container = remove_item(1, container)
    container is now [2, 3, 4]

    Dictionary: The key equal to the item is removed from the dictionary. The multi parameter is ignored. For example:

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    container = remove_item(2, container)
    container is now {1: 'a', 3: 'c', 4: 'd'}

    Set: The object that is equal to the item is removed from the set. The multi parameter is ignored. For example:

    container = {1, 2, 3, 4}
    container = remove_item(3, container)
    container is now {1, 2, 4}

    Tuple: All the objects in the tuple that are equal to the item are removed. If, the multi argument is set to False only the first occurrence is removed. For example:

    container = (1, 2, 3, 4)
    container = remove_item(4, container)
    container is now (1, 2, 3)

    '''
    if isinstance(container, list):
        if multi:
            for object in container:
                if object == item:
                    container.remove(object)
        else:
            container.remove(item)

    elif isinstance(container, dict):
        del container[item]

    elif isinstance(container, set):
        container.remove(item)

    elif isinstance(container, tuple):
        output = list(container)
        if multi:
            for object in output:
                if object == item:
                    output.remove(object)
        else:
            output.remove(item)
        container = tuple(output)
    
    return container

if __name__ == '__main__':

    assert remove_item(1, [1, 2, 3, 4, 1]) == [2, 3, 4]
    assert remove_item(1, [1, 2, 3, 4, 1], False) == [2, 3, 4, 1]
    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    assert remove_item(2, container) == {1: 'a', 3: 'c', 4: 'd'}
    assert remove_item(3, {1, 2, 3, 4}) == {1, 2, 4}
    assert remove_item(1, (1, 2, 3, 4, 1)) == (2, 3, 4)
    assert remove_item(1, (1, 2, 3, 4, 1), False) == (2, 3, 4, 1)