def convert_container(container: object, container_type: str) -> object:
    """
    Finally, you are going to implement the convert_container function that transforms any basic Python container (list, set, tuple, dict) to any of the basic container types.
    The function has the following parameters:

    container: The original container (list, set, tuple, dict) that is to be transformed to a new type.

    container_type: The str indicator of the type to which the container should be transformed ('list', 'set', 'tuple', 'dict').

    The function returns the new container transformed to a new type (container_type).

    Alternatively, if container's type matches that described by container_type, it returns the original, unmodified container.

    This is how the convert_container function handles transforming container to a new container_type for the individual container types:

    LIST:
    If container is of type list the conversions to the other three types should be handled as follows:

        List to List: The original container is returned.

        List to Dictionary: The elements of the list become keys in the new dict. In case of duplicate items, only the first one is added and the remaining ones are dropped.
        The keys are associated with None values. In the special case where the elements of the original list are tuples of len 2 the first element of the tuple is to be used
        as a key and the second as a value in the new dict. For example:

    container = [1, 2, 3, 4]
    new_container = convert_container(container, 'dict')
    # new_container is now {1: None, 2: None, 3: None, 4: None}

    container = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    new_container = convert_container(container, 'dict')
    # new_container is now {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

        To List to Set: The elements of the list become elements of the new set. In case of duplicate items, only the first one is added and the remaining ones are dropped.

    container = [1, 2, 3, 4]
    new_container = convert_container(container, 'set')
    # new_container is now {1, 2, 3, 4}

        List to Tuple: The elements of the list become elements of the new tuple. The order of elements is preserved.

    container = [1, 2, 3, 4]
    new_container = convert_container(container, 'tuple')
    # new_container is now (1, 2, 3, 4)

    DICT:

        Dictionart to Dictionary: The original container is returned.

        Dictionart to List: Key and value pairs of the original dict are transformed into (key, value) tuples and then inserted into the list. The order of elements is not
        important.

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    new_container = convert_container(container, 'list')
    # new_container is now [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

        Dictionart to Set: Key and value pairs of the original dict are transformed into (key, value) tuples and then inserted into the set.

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    new_container = convert_container(container, 'set')
    # new_container is now {(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')}

        Dictionart to Tuple: Key and value pairs of the original dict are transformed into (key, value) tuples and then inserted into the tuple. The order of elements is
        not important.

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    new_container = convert_container(container, 'tuple')
    # new_container is now ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

    SET:

        Set to Set: The original container is returned.

        Set to List: The elements of the set become elements of the new list. The order of elements is not important.

    container = {1, 2, 3, 4}
    new_container = convert_container(container, 'list')
    # new_container is now [1, 2, 3, 4]

        Set to Dictionary: The elements of the set become keys in the new dict. The keys are associated with None values. In the special case where the elements of the
        original set are tuples of len 2 the first element of the tuple is to be used as a key and the second as a value in the new dict.

    container = {1, 2, 3, 4}
    new_container = convert_container(container, 'dict')
    # new_container is now {1: None, 2: None, 3: None, 4: None}

    container = {(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')}
    new_container = convert_container(container, 'dict')
    # new_container is now {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

        Set to Tuple: The elements of the set become elements of the new tuple. The order of elements is not important.

    container = {1, 2, 3, 4}
    new_container = convert_container(container, 'tuple')
    # new_container is now (1, 2, 3, 4)

    TUPLE:

        Tuple to Tuple: The original container is returned.

        Tuple to List: The elements of the tuple become elements of the new list. The order of elements is preserved.

    container = (1, 2, 3, 4)
    new_container = convert_container(container, 'list')
    # new_container is now [1, 2, 3, 4]

        Tuple to Dictionary: The elements of the tuple become keys in the new dict. In case of duplicate items, only the first one is added and the remaining ones are
        dropped. The keys are associated with None values. In the special case where the elements of the original tuple are also tuples of len 2 the first element of the
        tuple is to be used as a key and the second as a value in the new dict.

    container = (1, 2, 3, 4)
    new_container = convert_container(container, 'dict')
    # new_container is now {1: None, 2: None, 3: None, 4: None}

    container = ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))
    new_container = convert_container(container, 'dict')
    # new_container is now {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

        Tuple to Set: The elements of the tuple become elements of the new set. In case of duplicate items, only the first one is added and the remaining ones are dropped.

    container = (1, 2, 3, 4)
    new_container = convert_container(container, 'set')
    # new_container is now {1, 2, 3, 4}

    """
    type_dict = {"list": [], "set": set(), "dict": {}, "tuple": ()}

    if type(type_dict[container_type]) == type(container):
        pass
    else:
        if isinstance(container, list):
            if container_type == "set":
                container = set(container)
            elif container_type == "tuple":
                container = tuple(container)
            elif container_type == "dict":
                output_dict = {}
                for index in container:
                    if type(index) == tuple and len(index) == 2:
                        key, value = index
                        output_dict[key] = value
                    else:
                        output_dict[index] = None
                container = output_dict
        elif isinstance(container, set):
            new_list = list(container)
            if container_type == "list":
                container = list(container)
            elif container_type == "tuple":
                container = tuple(container)
            elif container_type == "dict":
                output_dict = {}
                for index in new_list:
                    if type(index) == tuple and len(index) == 2:
                        key, value = index
                        output_dict[key] = value
                    else:
                        output_dict[index] = None
                container = output_dict
        elif isinstance(container, tuple):
            if container_type == "list":
                container = list(container)
            elif container_type == "set":
                container = set(container)
            elif container_type == "dict":
                output_dict = {}
                new_list = list(container)
                new_list.sort
                for index in new_list:
                    if type(index) == tuple and len(index) == 2:
                        key, value = index
                        output_dict[key] = value
                    else:
                        output_dict[index] = None
                container = output_dict

        elif isinstance(container, dict):
            new_list = []
            for key, value in container.items():
                new_list.append((key, value))
            if container_type == "list":
                container = new_list
            elif container_type == "set":
                container = set(new_list)
            elif container_type == "tuple":
                container = tuple(new_list)

    return container


if __name__ == "__main__":
    assert convert_container([1, 2, 3, 4], "dict") == {
        1: None,
        2: None,
        3: None,
        4: None,
    }
    assert convert_container([1, (2, "a"), 3, (4, "b")], "dict") == {
        1: None,
        2: "a",
        3: None,
        4: "b",
    }
    assert convert_container([1, 2, 3, 4], "set") == {1, 2, 3, 4}
    assert convert_container([1, 2, 3, 4], "tuple") == (1, 2, 3, 4)

    orig_dict = {1: "a", 2: "b", 3: "c", 4: "d"}
    new_list = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
    assert sorted(convert_container(orig_dict, "list")) == new_list

    orig_dict = {1: "a", 2: "b", 3: "c", 4: "d"}
    new_set = {(1, "a"), (2, "b"), (3, "c"), (4, "d")}
    assert convert_container(orig_dict, "set") == new_set

    orig_dict = {1: "a", 2: "b", 3: "c", 4: "d"}
    ref_tuple = ((1, "a"), (2, "b"), (3, "c"), (4, "d"))
    new_tuple = convert_container(orig_dict, "tuple")
    assert type(new_tuple) is tuple
    assert tuple(sorted(new_tuple)) == ref_tuple

    assert sorted(convert_container({1, 2, 3, 4}, "list")) == [1, 2, 3, 4]

    assert convert_container({1, 2, 3, 4}, "dict") == {
        1: None,
        2: None,
        3: None,
        4: None,
    }

    assert convert_container({1, (2, "a"), 3, (4, "b")}, "dict") == {
        1: None,
        2: "a",
        3: None,
        4: "b",
    }

    new_tuple = convert_container({1, 2, 3, 4}, "tuple")
    assert type(new_tuple) is tuple
    assert tuple(sorted(new_tuple)) == (1, 2, 3, 4)

    assert convert_container((1, 2, 3, 4), "list") == [1, 2, 3, 4]
    assert convert_container((1, 2, 3, 4), "dict") == {
        1: None,
        2: None,
        3: None,
        4: None,
    }
    assert convert_container((1, (2, "a"), 3, (4, "b")), "dict") == {
        1: None,
        2: "a",
        3: None,
        4: "b",
    }
    assert convert_container((1, 2, 3, 4), "set") == {1, 2, 3, 4}
