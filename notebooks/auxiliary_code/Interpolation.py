import numpy as np
from typing import List
from pandas import DataFrame
from auxiliary_code.helper_functions import *


class Interpolation:
    def __init__(self, df: DataFrame, columns: List[str], neighbours_dict: dict, epsilon: float = 1e-6) -> None:
        self.df = df[columns].copy()
        self.df_orig = df
        self.columns = columns
        self.epsilon = epsilon
        self.na_means = []
        self.areas = get_area(df).unique()
        self.neighbours_dict = neighbours_dict

    def interpolate_spatially(self):
        while True:
            na_mean = self.df[self.columns].isna().mean().to_numpy()
            self.na_means.append(na_mean)
            # stop if no no decrease in NA percentage has occured
            if (len(self.na_means) > 1) and (np.sum(self.na_means[-2] - self.na_means[-1]) < self.epsilon):
                break
            self.df = self.__spatial_interpolate_step()

        # drop original column values
        self.df_orig = self.df_orig.drop(self.columns, axis=1)
        # merge with new df
        self.df_orig = self.df_orig.merge(
            self.df, left_index=True, right_index=True)

        return self.df_orig

    def __spatial_interpolate_step(self):
        target_df = []
        for i, df in self.df.groupby('date'):
            # only keep area index (date is fixed here)
            df = df.droplevel(1)
            for area in self.areas:
                # target is a specific area, at a specific date, selected columns
                target = df.loc[area].squeeze()
                isna = target.isna()
                # if any of the columns are NA's replace them with the means
                # of their neighbours.
                if np.any(isna):
                    target.loc[isna] = df.loc[self.neighbours_dict[area], isna].mean()
                target_df.append(list(target) + [i] + [area])
        target_df = DataFrame(
            target_df, columns=self.columns + ['date', 'area'])
        set_index(target_df)
        return target_df

    def get_na_means(self):
        return np.array(self.na_means[:-1])


if __name__ == '__main__':
    import pandas as pd
    from os import getcwd

    price_columns = ['Sorghum prices', 'Maize prices', 'Red Rice prices']

    cwd = getcwd()
    path_fsnau = cwd + '\\datasets\\'
    path_shape = cwd + '\\geography\\Somalia\\Som_Admbnda_Adm2_UNDP.shp'
    df_fsnau = pd.read_csv(
        path_fsnau + 'fsnau_processed.csv', parse_dates=['date'])
    set_index(df_fsnau)
    neighbors_dict = get_neighbour_dict(get_shape_file(path_shape))
    interpolation = Interpolation(df_fsnau, price_columns, neighbors_dict)
    df_fsnau = interpolation.interpolate_spatially()
    print(df_fsnau.isna().mean())
    print(interpolation.get_na_means())
