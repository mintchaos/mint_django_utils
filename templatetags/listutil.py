"""
Template tags for working with lists.

You'll use these in templates thusly::

    {% load listutil %}
    {% for sublist in mylist|parition:"3" %}
        {% for item in mylist %}
            do something with {{ item }}
        {% endfor %}
    {% endfor %}
"""

from django import template

register = template.Library()

# @register.filter
def partition(thelist, n):
    """
    Break a list into ``n`` pieces. The last list may be larger than the rest if
    the list doesn't break cleanly. That is::

        >>> l = range(10)

        >>> partition(l, 2)
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

        >>> partition(l, 3)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

        >>> partition(l, 4)
        [[0, 1], [2, 3], [4, 5], [6, 7, 8, 9]]

        >>> partition(l, 5)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p*i:p*(i+1)] for i in range(n - 1)] + [thelist[p*(i+1):]]
register.filter(partition)

# @register.filter
def partition_horizontal(thelist, n):
    """
    Break a list into ``n`` peices, but "horizontally." That is, 
    ``partition_horizontal(range(10), 3)`` gives::
    
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10]]
        
    Clear as mud?
    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    newlists = [list() for i in range(int(ceil(len(thelist) / float(n))))]
    for i, val in enumerate(thelist):
        newlists[i/n].append(val)
    return newlists
register.filter(partition_horizontal)


# @register.filter
def partition_horizontal_twice(thelist, numbers):
    """
    numbers is split on a comma to n and n2.
    Break a list into peices each peice alternating between n and n2 items long 
    ``partition_horizontal_twice(range(14), "3,4")`` gives::
    
        [[0, 1, 2],
         [3, 4, 5, 6], 
         [7, 8, 9], 
         [10, 11, 12, 13]]
    
    Clear as mud?
    """
    n, n2 = numbers.split(',')
    try:
        n = int(n)
        n2 = int(n2)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    newlists = []
    while thelist:
        newlists.append(thelist[:n])
        thelist = thelist[n:]
        newlists.append(thelist[:n2])
        thelist = thelist[n2:]
    return newlists
register.filter(partition_horizontal_twice)

# @register.filter
def split(string, split_on=" "):
    """Splits a string just like the built in .split"""
    try:
        string = str(string)
        split_on = str(split_on)
    except (ValueError, TypeError):
        return [string]
    return string.strip('/').split(split_on)
register.filter(split)