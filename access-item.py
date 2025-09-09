def access_item(item: int, container):
    """
    Next, you are going to implement the access_item function that retrieves an item from any basic Python container (list, set, tuple, dict). The function has the following
    parameters:

    item: An integer value as

        * the index of the object to be retrieved from the container if the container is a list or a tuple;

        * the key of the value to be retrieved from the container if the container is a dict;

        * an object to be assessed if it is present in the container in case the container is a set.

    container: The container from which the item is retrieved (which can be list, set, tuple, dict).

    The function returns the element stored under the respective index (list, tuple) or key (dict), or it returns a bool indicating if the element is present in the container
    (set).

    This is how the access_item function should handle retrieving an item from the individual container types:

    List: The element under the item index is returned. For example:

    container = [1, 2, 3, 4]
    element = access_item(2, container)
    # element is now 3

    Dictionary: The value under the item key is returned. For example:

    container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    element = access_item(2, container)
    # element is now 'b'

    Set: A bool indicating if item is present in the set is returned. For example:

    container = {1, 2, 3, 4}
    element = access_item(2, container)
    # element is now True

    container = {1, 2, 3, 4}
    element = access_item(5, container)
    # element is now False

    Tuple: The element under the item index is returned. For example:

    container = (1, 2, 3, 4)
    element = access_item(1, container)
    # element is now 2

    """

    if isinstance(container, set):  # sets can not be indexed because they are unordered

        return item in container

    else:

        return container[item]


if __name__ == "__main__":

    assert access_item(2, [1, 2, 3, 4]) == 3
    container = {1: "a", 3: "c", 4: "d"}
    assert access_item(3, container) == "c"
    assert access_item(2, {1, 2, 3, 4}) == True
    assert access_item(5, {1, 2, 3, 4}) == False
    assert access_item(2, (1, 2, 3, 4)) == 3
