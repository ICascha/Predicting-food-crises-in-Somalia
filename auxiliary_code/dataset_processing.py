import pandas as pd


def process_world_bank(input_path: str, output_path) -> None:
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


if __name__ == '__main__':
    dataset_path = 'datasets/'
    process_world_bank(dataset_path + 'predicting_food_crises_data.csv',
                       dataset_path + 'world_bank_processed.csv')
