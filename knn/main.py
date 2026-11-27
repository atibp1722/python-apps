# import libraries
import numpy as np
import matplotlib.pyplot as plt

# same outcome on every execution
np.random.seed(42)

# knn class
class KNN:
    # intialize constructor with no. of neighbors
    def __init__(self, K):
        self.K = K
    # method to calculate eucldian disatnce
    def euclidianDistance(self, x1, x2):
        # intial distance
        distance = 0
        # iterate cand calculate distance between points
        for i in range(len(x1)):
            distance += np.power((x1[i] - x2[i]), 2)
        # square the distance
        return np.sqrt(distance)
    # method to predict outputs
    def knnSearch(self, X_train, y_train, Q):
        # store predictions
        y_pred = np.empty(Q.shape[0])
        # iterate each point
        for i, query in enumerate(Q):
            # sort distance and take top index
            index = np.argsort([self.euclidianDistance(query, x) for x in X_train])[:self.K]
            knn_labels = np.array([y_train[i] for i in index])
            # neigbor labels
            y_pred[i] = np.mean(knn_labels)
        return y_pred

if __name__ == "__main__":
    plt.close("all")
    # import libraries for dataset and train/test
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    # load iris dataset
    iris = datasets.load_iris()
    # take first 2 features
    X = iris.data[:, :2]
    y = iris.target
    # split data for train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # neaerst neighbor values
    K = 4
    # intialize object for knn class
    knn = KNN(K)
    # call method to make prediction
    y_pred = knn.knnSearch(X_train, y_train, X_test)
    # visualization
    plt.figure()
    # plot training and testing points
    plt.scatter(X_train[:, 0], X_train[:, 1], s=100, marker="x", color="g", label="data")
    plt.scatter(X_test[:, 0], X_test[:, 1], s=100, marker="o", color="b", label="query")
    # add titles and labels
    plt.title("K-Nearest Neighbors (K=%d)" %K)
    plt.legend()
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.grid(True)
    plt.show()