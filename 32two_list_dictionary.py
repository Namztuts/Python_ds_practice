def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    results = {}
    #example using     keys['x', 'y', 'z']   values[9, 8, 7])
    #enumerate just gives an index to each value; in this case, each key gets an index to associate with > [(0, 'x'), (1, 'y'), (2, 'z')]
    for i, val in enumerate(keys):
        #results[x] = values[0] (values at index 0 is 9) | puts x:9 key/val pair into the results dictionary > {'x':9}
        results[val] = values[i] if i < len(values) else 'No val'

    return results