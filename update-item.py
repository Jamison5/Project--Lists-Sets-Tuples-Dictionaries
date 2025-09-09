def update_item(
    orig_item: object, new_item: object, container: object, multi: bool = True
) -> object:
    """
    Next, you are going to implement the update_item function that updates an item in any of the basic Python containers (list, set, tuple, dict). The function has the
    following parameters:

    orig_item: The object to be updated.

    new_item: The object to replace the orig_item in the container.

    container: The container in which the item is updated (list, set, tuple, dict).

    multi: The bool specifier indicating if only the first occurrence of the item should be updated (False) or all of them (True). This parameter has a default value set
    to True.

    The function returns the updated container (or its copy if necessary).

    This is how the update_item function handles updating an item in the individual container types:

    List: All the objects in the list that are equal to the orig_item are replaced with the new_item. In case, the multi argument is set to False only the first occurrence
    is replaced. For example:

    container = [1, 2, 3, 4, 1]
    container = update_item(1, 9, container)
    # container is now [9, 2, 3, 4, 9]

    container = [1, 2, 3, 4, 1]
    container = update_item(1, 9, container, False)
    # container is now [9, 2, 3, 4, 1]

    Dictionary: The orig_item is expected to be a key that already exists in a dict. The new_item is expected to be a value that replaces the value associated with the
    orig_item key. In a special case of the new_item being a tuple with 2 elements, the first element is expected to be a new key and the second a new value. In that case
    the original key (orig_item) is removed, and the new value is added under the new key.

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    container = update_item(1, 'h', container)
    # container is now {1: 'h', 2: 'b', 3: 'c', 4: 'd'}

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    container = update_item(1, (9, 'e'), container)
    # container is now {9: 'e', 2: 'b', 3: 'c', 4: 'd'}

    Set: The orig_item is removed from the set and the new_item is added.

    container = {1, 2, 3, 4, 5}
    container = update_item(5, 9, container)
    # container is now {1, 2, 3, 4, 9}

    Tuple: All the objects in the tuple that are equal to the orig_item are replaced with the new_item. If, the multi argument is set to False only the first occurrence
    is replaced. For example:

    container = (1, 2, 3, 4, 1)
    container = update_item(1, (9, 11), container)
    # container is now ((9, 11), 2, 3, 4, (9, 11))

    container = (1, 2, 3, 4, 1)
    container = update_item(1, (9, 11), container, False)
    # container is now ((9, 11), 2, 3, 4, 1)

    """
    if isinstance(container, list):
        if multi:
            for index, _ in enumerate(container):
                if container[index] == orig_item:
                    container[index] = new_item
        else:
            orig_item_index = container.index(orig_item)
            container[orig_item_index] = new_item

    elif isinstance(container, dict):
        if (
            "__len__" in dir(new_item)
            and len(new_item) == 2
            and isinstance(new_item, tuple)
        ):
            new_key, new_value = new_item
            new_dict = {}
            for key, value in container.items():
                if key == orig_item:
                    new_dict[new_key] = new_value
                else:
                    new_dict[key] = value
            container = new_dict
        else:
            container[orig_item] = new_item

    elif isinstance(container, set):
        if orig_item in container:
            container.remove(orig_item)
            container.add(new_item)

    return container


if __name__ == "__main__":

    container = {1, 2, 3, 4, 5}
    container = update_item(5, 9, container)
    # container is now {1, 2, 3, 4, 9}
    print(container)
