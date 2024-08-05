def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
        # mode([1, 2, 1]); using first index (1) as example
    for num in nums:
        #    key           value
        # counts[1] = counts.get(1,0)+1
        # if num is found        add 1 to it
        counts[num] = counts.get(num, 0) + 1

        #max_value = max([2,1])
    max_value = max(counts.values())
        #max_value = 2
        #counts.items([(1, 2), (2, 1)])
    for (num, freq) in counts.items():
        #              counts.items([(1, 2), (2, 1)])
        #if the second item in each tuple is equal to the max (2), return the num
        #in this case, the first set (1,2) (freq) is 2 and is equal to the max, so it is returned
        if freq == max_value:
            return num
    
        
