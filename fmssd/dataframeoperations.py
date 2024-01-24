import pandas as pd


def check_if_significant(data_in, thresh):
    """
    check if variance of a column is above threshold
    takes: dataframe, threshold
    returns: dataframe with columns with variance above threshold
    """
    data_out = data_in.drop(data_in.var()[data_in.var() < thresh].index.values, axis=1)
    indices = data_in.var()[data_in.var() > thresh].index.values
    return data_out, indices


# take get_correltation_measure() from techer's solution
# add surrounding code into this function
def get_correlation(df):
    """
    get rid of time column, lower triangular and diagonal entries of the correlation matrix
    takes: dataframe with time column
    returns: sorted correlations
    """
    df = df.drop(["time"], axis=1)
    drop_values = set()  # an unordered collection of items
    cols = df.columns  # get the column labels
    print(cols)
    for i in range(0, df.shape[1]):
        for j in range(
            0, i + 1
        ):  # get rid of all diagonal entries and the lower triangular
            drop_values.add((cols[i], cols[j]))
    corr = df.corr().unstack()  # pivot the correlation matrix
    # sort by absolute values but keep sign
    corr = corr.drop(labels=drop_values).sort_values(
        ascending=False, key=lambda col: col.abs()
    )
    return corr
