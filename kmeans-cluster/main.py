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
        self.n_samples, self.n_features = X.shape
        random_sample_index = np.random.choice(self.n_samples, self.K, replace=False)
        self.centroids = [self.X[index] for index in random_sample_index]
        # iterate to define clusters
        for _ in range(self.max_iters):
            # assign neaerst centroid to data
            self.clusters = self._createClusters(self.centroids)
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
    # method to create clusters
    def _createClusters(self, centroids):
        # create empty list to store index
        clusters = [[] for _ in range(self.K)]
        # iterate each sample
        for index, sample in enumerate(self.X):
            # get closest centroid of the sample
            centroid_index = self._closestCentroid(sample, centroids)
            # append index to list
            clusters[centroid_index].append(index)
        return clusters
    # method to assign closest centroid
    def _closestCentroid(self, sample, centroids):
        # calculate distance from sample to centroid
        distance = [eucledianDistance(sample, point) for point in centroids]
        # get index of minimum distance
        closest_index = np.argmin(distance)
        return closest_index
    # method to get centroids
    def _getCentroids(self, clusters):
        centroids = np.zeros((self.K, self.n_features))
        # iterate each cluster and its index
        for cluster_index, cluster in enumerate(clusters):
            # calcluate mean 
            cluster_mean = np.mean(self.X[cluster], axis=0)
            # assign to centroid
            centroids[cluster_index] = cluster_mean
        return centroids
    # method to check if centroids are converged
    def _isConverged(self, old_centroids, centroids):
        # calculate distance moved by each centroid
        distance = [eucledianDistance(old_centroids[i], centroids[i]) for i in range(self.K)]
        # true if movement of all centroids is 0
        return sum(distance) == 0
    # method to plot values
    def plot(self):
        plt.close("all")
        # cluster and centroids to plot
        fig, ax = plt.subplots(figsize=(10, 5))
        # iterate all cluster index
        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)
        # iterate all centroids
        for point in self.centroids:
            ax.scatter(*point, marker="x", color="green", linewidth=2)
        plt.show()

if __name__ == "__main__":
    # same result on every execution
    np.random.seed(42)
    # import dataset
    from sklearn.datasets import make_blobs
    X, y = make_blobs(centers=3, n_samples=500, n_features=2, shuffle=True, random_state=42)
    # display dimension
    print(X.shape)
    # display unique clusters
    clusters = len(np.unique(y))
    print(clusters)
    # object to intialize class and its emthods
    kmns = KMeans(K=clusters, max_iters=100, plot_steps=False)
    # make and plot predictions
    y_pred = kmns.predict(X)
    kmns.plot() 