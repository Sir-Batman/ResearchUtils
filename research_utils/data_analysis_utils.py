import pandas as pd
import numpy as np


def statruns_to_multiindex(df1, df2, *args, ignore_size=False):
    """
    Takes in at least 2 dataframes (which are statistical runs of the same data) and returns a multi-index of
    the data so that plotting, averages, and means are much more easily calculated

    :param df1: First dataframe
    :param df2: Second dataframe
    :param args: additional dataframes
    :param ignore_size: Do not raise error if the size of the first index varies between dataframes
    :return: new dataframe with multi-index for the original input data (generations, timesteps, etc) and one differentiating stat runs
    :raises: error on dataframes not having the same columns, or not having the same type of original input.
    """
    # TODO use ignore_size param
    # TODO raise error on dataframes not having sames columns or type mismatches
    modified_dfs = []
    for i, df in enumerate([df1, df2] + list(args)):
        modified_dfs.append(df.set_index(pd.MultiIndex.from_product([[i], df.index])))
    out = pd.concat(modified_dfs)
    names = list(out.index.names)
    names[0] = "Stat Run"
    out.index.rename(names, inplace=True)
    return out


def statrun_mean_error(df1, df2, *args):
    """
    Converts at least 2 dataframes of statistical runs of the same simulation data and returns the mean and standard
    deviation across statistical runs

    :param df1: Statrun 1
    :param df2: Statrun 2
    :param args: Statruns 3+
    :return: Dataframes for the mean and standard deviations across statistical runs
    """
    combined = statruns_to_multiindex(df1, df2, *args)
    return combined.mean(level=1), combined.std(level=1)


def map_number_ranges(x, old_min, old_max, new_min, new_max):
    """
    Converts a number that exists in the range [old_min, old_max] to the range [new_min, new_max]

    :param x: the number to convert
    :param old_min: current number range minimum value
    :param old_max: current number range maximum value
    :param new_min: new range minimum value
    :param new_max: new range maximum value
    :return: float: number converted into the range [new_min, new_max]
    """
    return (((x - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min


if __name__ == '__main__':
    df1 = pd.DataFrame(data=[[1, 2], [3, 4], [5, 6]], columns=["Col A", "Col B"])
    df2 = pd.DataFrame(data=[[10,20], [30, 40], [50, 60], [70, 80]], columns=["Col A", "Col B"])
    out = statruns_to_multiindex(df1, df2)
    print(out)
    mean, std = statrun_mean_error(df1, df2)
    print(mean)
    print(std)
