from scipy.stats import percentileofscore as pctofscore

from copy import deepcopy


def percentileofscore(values):

    percentiles = [0] * len(values[0])

    num_rows = len(values)

    for row_index in range(num_rows):

        row_vals = values[row_index]

        for col_index, col_val in enumerate(row_vals):

            percentiles[col_index] = pctofscore(row_vals, col_val)

        values[row_index] = percentiles
