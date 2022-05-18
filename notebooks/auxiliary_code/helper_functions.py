from pandas import DataFrame, Index
from geopandas import read_file, GeoDataFrame


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


def get_shape_file(path: str) -> GeoDataFrame:
    """get the shapefile of Somalia.

     Args:
        path (str): the path to the shapefile

    Returns:
        GeoDataFrame: shapefile of Somalia.
    """
    df = read_file(path)
    df['area'] = df['admin2Name'].str.lower()
    df.drop(['admin2Name'], axis=1, inplace=True)
    return df.set_index('area')


def get_neighbour_dict(df: GeoDataFrame) -> dict:
    """get a mapping of an area to its neighbors.

    Args:
        df (GeoDataFrame): shape dataframe.

    Returns:
        dict: mapping of an area to a list of its neighbors.
    """
    neighbors_dict = dict()
    for i, row in df.iterrows():
        neighbors = df[df.geometry.touches(
            row['geometry'])].index.tolist()
        neighbors_dict[i] = neighbors
    return neighbors_dict
