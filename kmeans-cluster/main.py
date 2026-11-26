# import libraries
import numpy as np
import matplotlib.pyplot as plt

# function for eucledian distance
# sum of squared difference between x1 & x2
def eucledianDistance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# KMeans clustering class
class KMeans:
    # initialize constructor with hyper parameters
    def __init__(self, K=5, max_iters=100, plot_steps=False):
        self.K = K
        self.max_iters = max_iters
        self.plot_steps = plot_steps
        self.clusters = [[] for _ in range(self.K)]
        self.centroids = []
    # method to predict X on given data
    def predict(self, X):
        # store input
        self.X = X
        # samples and features
        self.n_samples = X.shape
        self.n_features = X.shape
        random_sample_index = np.random.choice(self.n_samples, self.K, replace=False)
        self.centroids = [self.X[index] for index in random_sample_index]
        # iterate to define clusters
        for _ in range(self.max_iters):
            # assign neaerst centroid to data
            self.clusters = self.createClusters(self.centroids)
            if (self.plot_steps):
                self.plot()
            # save old centroid values to update later
            old_centroids = self.centroids
            # update centroids
            self.centroids = self._getCentroids(self.clusters)
            # stop if centroids converge and dont move
            if (self._isConverged(old_centroids, self.centroids)):
                break
            if (self.plot_steps):
                self.plot()
        return self._getClusterLabels(self.clusters)
    # method to define labels for clusters
    def _getClusterLabels(self, clusters):
        labels = np.empty(self.n_samples)
        # iterate each cluster
        for cluster_index, cluster in enumerate(clusters):
            # iterate sample index belonging to luster
            for sample_index in cluster:
                # assign cluster index label
                labels[sample_index] = cluster_index
        return labels
