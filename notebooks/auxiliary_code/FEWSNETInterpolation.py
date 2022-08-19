from geopandas import read_file
from pandas import to_datetime
from os import listdir
from numpy import any


class Interpolation:
    def __init__(self, epsilon, files_path, df_shape) -> None:
        self.epsilon = epsilon
        self.files_path = files_path
        self.df_shape = df_shape

    def interpolate(self):
        columns = ['CS', 'HA0']
        results = {col: list() for col in columns}

        fews_net_files = filter(lambda f: f.endswith(
            '.shp'), listdir(self.files_path))
        for file in fews_net_files:
            df_geo = read_file(self.files_path + file)
            date = to_datetime(file[3:9], format='%Y%m')

            for area, row in self.df_shape.iterrows():
                polygon = row['geometry']
                intersect = df_geo['geometry'].intersects(polygon, align=False)

                if not any(intersect):
                    continue
                intersect_area = df_geo['geometry'].intersection(
                    polygon, align=False).area

                for column in columns:
                    if not column in df_geo.columns:
                        continue
                    weights, classification = self.__calculate_weights(
                        column, intersect_area, df_geo)
                    if weights is None:
                        continue
                    weighted_average, maximum = self.__calculate_result(
                        weights, classification)

                    results[column].append(
                        (area, date, weighted_average, maximum))
        return results

    def __calculate_weights(self, column, intersect_area, df_geo):
        mask = df_geo[column] > 5
        weights = intersect_area/intersect_area.sum()
        # if more than epsilon*100% of intersection is with unknown classification
        if weights[mask].sum() > self.epsilon:
            return None, None
        # re-normalize intersections with unknown area removed.
        weights = weights[~mask]
        weights = weights/weights.sum()
        return weights, df_geo[column][~mask]

    def __calculate_result(self, weights, classification):
        weighted_average = weights @ classification
        maximum = classification.iloc[weights.argmax()]
        return weighted_average, maximum
