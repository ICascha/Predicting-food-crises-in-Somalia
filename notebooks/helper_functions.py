from pandas import DataFrame, Index


def set_index(df: DataFrame) -> None:
    """set index of dataframe according to '[area, date]'
    format

    Args:
        df (df): input dataframe
    """
    if df.index.names and df.index.names == ['area', 'date']:
        return
    df.set_index(['area', 'date'], inplace=True)


def get_area(df: DataFrame) -> Index:
    """get area index of dataframe.

    Args:
        df (DataFrame): input dataframe

    Returns:
        Index: area index
    """
    return df.index.get_level_values(0)


def get_date(df: DataFrame) -> Index:
    """get date index of dataframe

    Args:
        df (DataFrame): input dataframe

    Returns:
        Index: date index
    """
    return df.index.get_level_values(1)
