# libraries to import
import numpy as np
import matplotlib.pyplot as plt
# 42 so result is same every time it is run
np.random.seed(42)

# class for pca
class PCA:
    # initialize constructor
    def __init__(self, n_components=2):
        # default no. of components
        self.n_components = n_components
    # method for covariance between X & Y
    def covarianceMatrix(self, X, Y=None):
        if (Y is None):
            Y = X
        # get samples
        n_samples = np.shape(X)[0]
        # calculate the covariance
        covarianceMatrix = (1 / (n_samples -1)) * (X - X.mean(axis=0)).T.dot(Y - Y.mean(axis=0))
        return covarianceMatrix
    # method to transform into principal dimensions
    def transform(self, X):
        # covariance of input
        sigma = self.covarianceMatrix(X)
        # calculate eigen values and vectors of matrix
        eigen_values, eigen_vectors = np.linalg.eig(sigma)
        # sort eigen values
        index = eigen_values.argsort()[::-1]
        # sort and keep top components
        eigen_values = eigen_values[index][:self.n_components]
        # match eigen vectors with their eigen values
        eigen_vectors = np.atleast_1d(eigen_vectors[:, index])[:, :self.n_components]
        # make projections
        X_transform = X.dot(eigen_vectors)
        return X_transform

# no. of data
n = 20
# no. of features
d = 5
X = np.random.rand(n, d)
# create object to initialize class
pca = PCA(n_components=2)
# fit data to pca matrix
X_pca = pca.transform(X)
print(X_pca)
# create plot
plt.figure()
# actual plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], color="g", alpha=0.5)
# set title and labels
plt.title("Principal Component Analysis (PCA)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()