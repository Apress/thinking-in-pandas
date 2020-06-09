def percentileofscore(a, score):
    """

    Three-quarters of the given values lie below a given score:

    >>> stats.percentileofscore([1, 2, 3, 4], 3)

    75.0



    With multiple matches, note how the scores of the two

    matches, 0.6 and 0.8 respectively, are averaged:

    >>> stats.percentileofscore([1, 2, 3, 3, 4], 3)

    70.0

    """

    n = len(a)

    left = np.count_nonzero(a < score)

    right = np.count_nonzero(a <= score)

    pct = (right + left + (1 if right > left else 0)) * 50.0 / n

    return pct
