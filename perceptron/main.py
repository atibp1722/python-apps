import numpy as np

# activation function that triggers neuron 
# value range(0, 1); 1 tells to fire 0 tells no fire
def stepFunction(x):
    return np.where(x > 0, 1, 0)

# perceptron class
class Perceptron:
    # initialize constructor
    # parameters for learn rate and no. of iterations to run
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.learn_rate = learning_rate
        self.n_iters = n_iters
        self.activationFunction = stepFunction
        # intial weights and bias are None
        # updated during fit
        self.weights = None
        self.bias = None
    # method to train perceptron
    def fit(self, X, y):
        n_samples, n_features = X.shape
        # initialize weight and bias vectors
        self.weights = np.zeros(n_features)
        self.bias = 0
        # iterate all samples
        for _ in range(self.n_iters):
            # iterate each sample with index
            for index, x_i in enumerate(X):
                # calculating z  = w * x + b 
                # pre activation value of neuron
                linear_output = np.dot(x_i, self.weights) + self.bias
                # feed to activation function
                y_predict = self.activationFunction(linear_output)
                update = self.learn_rate * (y[index] - y_predict)
                # update weights and bias
                self.weights += update * x_i
                self.bias += update
    # method to make predictions for data samples
    def predict(self, X):
        # linear output for all rows
        linear_output = np.dot(X, self.weights) + self.bias
        # map to activation function
        y_predict = self.activationFunction(linear_output)
        return y_predict

if __name__ == "__main__":
    # import ibraries for visualization
    import matplotlib.pyplot as plt
    # import library to train, test and for dataset
    from sklearn.model_selection import train_test_split
    from sklearn import datasets
    # method to calculate accuracy
    def accuracy(y_true, y_pred):
        # correct predictions divided by total
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy
    # generate data points
    X, y = datasets.make_blobs(n_samples=150, n_features=2, cluster_std=1.05, random_state=42)
    # split to 80-20 for train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # create object perceptron class and initialize it
    pcptn = Perceptron(learning_rate=0.01, n_iters=1000)
    # train data
    pcptn.fit(X_train, y_train)
    # predict data labels
    prediction = pcptn.predict(X_test)
    # model accuracy
    print("perceptron accuracy:", accuracy(y_test, prediction))
    # visualization
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # data points in scatter plot
    plt.scatter(X_train[:, 0], X_train[:, 1], marker="x", c=y_train)
    # min and max value features
    x0_1 = np.amin(X_train[:, 0])
    x0_2 = np.amax(X_train[:, 0])
    # points for decision boundary
    x1_1 = (-pcptn.weights[0] * x0_1 - pcptn.bias) / pcptn.weights[1]
    x1_2 = (-pcptn.weights[0] * x0_2 - pcptn.bias) / pcptn.weights[1]
    # decision boundary plot
    ax.plot([x0_1, x0_2], [x1_1, x1_2], "k")
    # min and max value of features
    ymin = np.amin(X_train[:, 1])
    ymax = np.amax(X_train[:, 1])
    ax.set_ylim([ymin - 3, ymax + 3])
    plt.show()