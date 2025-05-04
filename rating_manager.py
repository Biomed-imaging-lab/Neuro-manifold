import numpy as np
from sklearn.metrics import pairwise_distances

class RatingManager:
    def intracluster_distance(self, cluster, method='mean'):
        """
        Calculate the intracluster distance between points in a given cluster.

        Parameters:
        cluster (numpy.ndarray): A 2D array representing the points in the cluster.
        method (str): The method to calculate the intracluster distance. It can be either 'mean' or 'median'. Default is 'mean'.

        Returns:
        float: The intracluster distance. If the cluster contains only one point, it returns 0.
        """

        if len(cluster) > 1:
            dist_matrix = pairwise_distances(cluster)
            sum_distances = np.sum(dist_matrix) / 2
            num_distances = len(cluster) * (len(cluster) - 1) / 2
            intra_distance = sum_distances / num_distances
        else:
            return 0

        if method == 'mean':
            return intra_distance
        elif method == 'median':
            return np.median(dist_matrix[np.triu_indices_from(dist_matrix, k=1)])
        else:
            raise ValueError('Invalid method')
        

    def intercluster_distance(self, cluster1, cluster2, method='mean'):
        if method == 'mean':
            centroid1 = np.mean(cluster1, axis=0)
            centroid2 = np.mean(cluster2, axis=0)
        elif method == 'median':
            centroid1 = np.median(cluster1, axis=0)
            centroid2 = np.median(cluster2, axis=0)
    
        return np.linalg.norm(centroid1 - centroid2)
