def freq_counter(coll):
    """Returns frequency counter mapping of coll."""

    results = {}

    for num in coll:
        results[num] = results.get(num, 0) + 1
    return results


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    #must turn numbers into a string in order to iterate over them
    #even if the dictionary values are out of order, they can still be equal
    return freq_counter(str(num1)) == freq_counter(str(num2))
    # same_frequency(1212, 2211)
    # {'1': 2, '2': 2} == {'2': 2, '1': 2} | True