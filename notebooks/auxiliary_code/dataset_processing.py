import pandas as pd
from numpy import nan


def process_world_bank(input_path: str, output_path: str) -> None:
    """process the world bank data. Removing uneccesary data
    and renaming columns.

    Args:
        input_path (str): input path to worldbank csv
        output_path (str): output path to processed csv
    """
    df = pd.read_csv(input_path)
    df = df[df['country'] == 'Somalia']
    df['date'] = pd.to_datetime(df['year_month'], format='%Y_%m')
    df.rename({'area': 'surface_area'}, axis=1, inplace=True)
    df['area'] = df['admin_name'].str.lower()
    df.drop(['admin_code', 'country', 'year_month',
            'year', 'month', 'admin_name'], axis=1, inplace=True)
    df.to_csv(output_path, index=False)


def process_fsnau(input_path: str, output_path: str, cutoff: float = 1e-3) -> None:
    """process the fnsau data. Filter outliers and rename columns

    Args:
        input_path (str): input path to fsnau csv
        output_path (str): output path to fsnau csv
        cutoff (float, optional): Ratio of observations to cutoff. Defaults to 1e-3.
    """
    df = pd.read_csv(input_path, parse_dates=['date'])
    epsilon = 10e-4

    def f(x):
        if type(x) != str:
            return nan
        i, j = x.split(' - ')
        return 0.5 * int(i) + 0.5 * int(j)

    df['Displacement (arrivals)'] = df['Displacement (arrivals)'].apply(
        f)
    df['Displacement (departures)'] = df['Displacement (departures)'].apply(
        f)
    df['Red Rice prices'] = df['Red Rice prices'].astype('float')
    df.drop(['Regions', 'Rainfall', 'Vegetation cover (NDVI)'],
            axis=1, inplace=True)
    df['Districts'] = df['Districts'].str.lower()
    df['Districts'] = df['Districts'].replace(
        {'mogadishu': 'banadir'})
    df.rename({'Districts': 'area'}, axis=1, inplace=True)
    price_columns = ['Price of water', 'Sorghum prices', 'Maize prices',
                     'Red Rice prices', 'Local goat prices', 'Cost of Minimum Basket (CMB)']
    mask = df[price_columns] >= df[price_columns].quantile(.999)
    mask = mask | (df[price_columns] < epsilon)

    for col in price_columns:
        df.loc[mask[col], col] = nan

    df.to_csv(output_path, index=False)


def process_ipc(input_path: str, output_path: str, cutoff: float = 1e-3) -> None:
    """Process IPC csv. Area names to lowercase.

    Args: 
        input_path (str): input path to ipc csv
        output_path (str): output path to ipc csv
    """
    df = pd.read_csv(input_path, parse_dates=['date'])
    df['area'] = df['area'].str.lower()
    df.to_csv(output_path, index=False)


def process_locations(input_path: str, output_path: str) -> None:
    """Process locations csv. Remove duplicates and rename columns.

    Args:
        input_path (str): input path to locations csv
        output_path (str): output path to processed locations csv
    """
    df = pd.read_csv(input_path).drop(
        'date', axis=1).drop_duplicates().iloc[:-1]
    df['area'] = df['district'].str.lower()
    df['area'].replace({'mogadishu': 'banadir'}, inplace=True)
    df.drop(['district'], axis=1, inplace=True)
    df.to_csv(output_path, index=False)


def process_production(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path, parse_dates=['date'])
    df['area'] = df['district'].str.lower()
    df['area'].replace({'ceel bur': 'ceel buur', 'el berde': 'ceel barde',
                       'garbaharey/burdhuubo': 'garbahaarey'}, inplace=True)
    df.drop(['district'], axis=1)
    df = df[df['area'] != 'hagar']
    df.to_csv(output_path, index=False)


if __name__ == '__main__':
    path = 'datasets/'
    process_world_bank(path + 'predicting_food_crises_data.csv',
                       path + 'world_bank_processed.csv')
    process_fsnau(path + 'fsnau_full.csv',
                  path + 'fsnau_processed.csv')
    process_ipc(path + 'ipc.csv', path + 'ipc_processed.csv')
    process_locations(path + 'locations.csv', path + 'locations_processed.csv')
    process_production(path + 'production.csv', path +
                       'production_processed.csv')
