def create_container(container_type: str) -> None:
    '''
    
    First, you are going to implement the create_container function that creates an empty Python data container (list, set, tuple, dict). The function has the 
    container_type parameter which a str indicating what type of container should be created ('list', 'set', 'tuple', 'dict').

    The function returns a new empty data container of the type indicated by container_type. Specifically:

    container = create_container('list')
    # container is now []

    container = create_container('dict')
    # container is now {}

    container = create_container('set')
    # container is now set()

    container = create_container('tuple')
    # container is now ()

    '''
    container = None

    if container_type.lower() == 'list':

        container = []

    elif container_type.lower() == 'dict':

        container = {}

    elif container_type.lower() == 'set':

        container = set()

    elif container_type.lower() == 'tuple':

        container = ()

    else:

        print('Please enter a vlaid, in-built data structure type.')

    return container

if __name__ == '__main__':

    test1 = create_container('list')
    test2 = create_container('dict')
    test3 = create_container('set')
    test4 = create_container('tuple')

    print(f'Data types created: {type(test1)}, {type(test2)}, {type(test3)}, {type(test4)}')