import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from sklearn.cluster import KMeans
from pandas import DataFrame

cmap = plt.get_cmap('tab10')


class Clustering:
    def __init__(self, cluster_sizes: list, seed: int):
        self.cluster_sizes = cluster_sizes
        self.seed = seed

    def spatial_clustering(self, areas, values, dates, df_shape,  xlab=None, ylab=None):
        fig, axs = plt.subplots(nrows=len(
            self.cluster_sizes), ncols=3, figsize=(20, 3.3 * len(self.cluster_sizes)))
        for n in self.cluster_sizes:

            kmeans = KMeans(n_clusters=n, random_state=self.seed).fit(values)
            clusters = kmeans.predict(values)
            df_cluster = DataFrame(
                {'area': areas, 'cluster': clusters}).set_index('area')
            df_plot = df_shape.merge(
                df_cluster, left_index=True, right_index=True)
            self.__plot_spatial_clustering(
                values, clusters, df_plot, dates, axs, n)

        axs[0, 0].set_title('clusters', size=20)
        axs[0, 1].set_title('discrict-level trends', size=20)
        axs[0, 2].set_title('cluster-level trends', size=20)

        if ylab:
            for i in range(len(self.cluster_sizes)):
                axs[i, 1].set_ylabel(ylab, size=14)
        if xlab:
            axs[-1, 1].set_xlabel(xlab, size=14)
            axs[-1, 2].set_xlabel(xlab, size=14)
                
        locator = mdate.YearLocator()
        for i in range(len(self.cluster_sizes)):
            axs[i, 1].xaxis.set_major_locator(locator)
            axs[i, 2].xaxis.set_major_locator(locator)
        
        plt.minorticks_off()

        return fig

    def __plot_spatial_clustering(self, values, clusters, df_plot, dates, axs, n):

        df_plot.plot(column='cluster', cmap='tab10',
                     ax=axs[n-2, 0], scheme='User_Defined', classification_kwds=dict(bins=range(9)))
        for i in range(n):
            axs[n-2, 1].plot(dates, values[clusters == i].T,
                             alpha=0.2, c=cmap(i))
            axs[n-2, 2].plot(dates, values[clusters ==
                                           i].T.mean(axis=1), c=cmap(i))
        axs[n-3, 0].axis('off')


if __name__ == '__main__':
    from os import getcwd
    import pandas as pd
    from helper_functions import *

    cwd = getcwd()
    path_ipc = cwd + '\\datasets\\ipc_processed.csv'
    path_shape = cwd + '\\geography\\Somalia\\Som_Admbnda_Adm2_UNDP.shp'

    df_phase = pd.read_csv(path_ipc, parse_dates=['date'], usecols=[
                           'date', 'area', 'area_phase'])

    set_index(df_phase)
    df_phase_unstacked = df_phase.unstack()
    mask = df_phase_unstacked.isna().sum(axis=1) == 0
    df_phase_unstacked = df_phase_unstacked[mask]
    dates = df_phase_unstacked.columns.get_level_values(1)
    areas = df_phase_unstacked.index
    values = df_phase_unstacked.to_numpy()

    clustering = Clustering(range(2, 5), 1337)
    clustering.spatial_clustering(
        areas, values, dates, get_shape_file(path_shape))
