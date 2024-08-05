def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

    return count
'''
example: [1, 2, 3]
len(nums) = 3
i      i+1        range(i+1,len(nums))    j
0       1         range(1,3)              1
1       2         range(2,3)              2
2       3         range(3,3)

if nums[1] > nums[0]
      2    >    1
since num[1] is greater than num[0] in this case, add 1 to the count
'''