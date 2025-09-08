def add_item(item, container, position=None):
    '''
    Next, you are going to implement the add_item function that adds an item to any basic Python container (list, set, tuple, dict). The function has the following parameters:

    item: The object to be inserted into the container. The item is expected to be of any type that can be added to the respective container.

    container: The container to which the item is added (list, set, tuple, dict).

    position: An int defining the position within the container to which the item should be inserted. This parameter has a default value set to None.

    The function returns the updated container (or its copy if necessary).

    This is how the add_item function handles adding an item to the individual container types:

    List: The item is appended to the end of the list. If, the optional position argument is provided, the item is inserted at that position. For example:

    container = [1, 2, 3, 4]
    container = add_item(9, container)
    # container is now [1, 2, 3, 4, 9]

    container = [1, 2, 3, 4]
    container = add_item((9, 11), container, 1)
    # container is now [1, (9, 11), 2, 3, 4]

    Dictionary: The item is added as a key in the dict and it is associated with the value of None. In a special case, where the item is a tuple of length 2 (i.e., it consists
    of 2 elements), the first element is used as the key and the second as the value. The optional position parameter is ignored even if provided. For example:

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    container = add_item(9, container)
    # container is now {1: 'a', 2: 'b', 3: 'c', 4: 'd', 9: None}

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    container = add_item((9, 'e'), container, 1)
    # container is now {1: 'a', 2: 'b', 3: 'c', 4: 'd', 9: 'e'}

    Set: The item is added to the set. The optional position parameter is ignored even if provided.

    container = {1, 2, 3, 4}
    container = add_item(9, container)
    # container is now {1, 2, 3, 4, 9}

    Tuple: The item is appended to the end of the tuple. If, the optional position argument is provided, the item is inserted at that position.

    container = (1, 2, 3, 4)
    container = add_item((9, 11), container, 1)
    # container is now (1, (9, 11), 2, 3, 4)

    '''
    if isinstance(container, list):
        
        if position == None:            
            container.append(item)
        else:
            container.insert(position, item)

    else:

        pass

if __name__ == '__main__':

    container = [1, 2, 3, 4]
    container = add_item(9, container)
    # container is now [1, 2, 3, 4, 9]
    print(container)

    container = [1, 2, 3, 4]
    container = add_item((9, 11), container, 1)
    # container is now [1, (9, 11), 2, 3, 4]
    print(container)