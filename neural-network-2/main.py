import numpy as np

# sigmoid activation function
# x = 1 / (1 + e^(-x))
# values fall between (0, 1)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# function for derivative of sigmoid
# d'(x) = sigmoid(x) * (1 - sigmoid(x))
def derivativeSigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)

# function for mse loss
def mseLoss(y_true, y_pred):
    # convert into numpy arrays
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    # squared difference between actual and predicted values
    return ((y_true - y_pred) ** 2).mean()

class NeuralNetwork:
    def __init__(self):
        # intializing weights from a normal distribution
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        # intializing biases from a normal distribution
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
    # method for forward propagation
    def forwardPropagation(self, x):
        # calcualate activations
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1
    # method for training via gradient descent
    def train(self, data, all_y_trues):
        # learning rate
        learning_rate = 0.1
        # number of epochs to run
        epochs = 1000
        for epoch in range(epochs):
            # iterate over sample and target
            for x, y_true in zip(data, all_y_trues):
                # forward propgation
                # weighted sums fo h1
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)
                # weighted sums fo h1
                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                # weighted sums for output
                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                # prediction for sample
                y_pred = o1
                # backward propagation
                # derivative of squared error with respect to y_pred
                d_L_d_ypred = -2 * (y_true - y_pred)
                # neuron o1
                d_ypred_d_w5 = h1 * derivativeSigmoid(sum_o1)
                d_ypred_d_w6 = h2 * derivativeSigmoid(sum_o1)
                d_ypred_d_b3 = derivativeSigmoid(sum_o1)
                d_ypred_d_h1 = self.w5 * derivativeSigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * derivativeSigmoid(sum_o1)
                # neuron h1
                d_h1_d_w1 = x[0] * derivativeSigmoid(sum_h1)
                d_h1_d_w2 = x[1] * derivativeSigmoid(sum_h1)
                d_h1_d_b1 = derivativeSigmoid(sum_h1)
                # neuron h2
                d_h2_d_w3 = x[0] * derivativeSigmoid(sum_h2)
                d_h2_d_w4 = x[1] * derivativeSigmoid(sum_h2)
                d_h2_d_b2 = derivativeSigmoid(sum_h2)
                # update weights and bias for the neurons
                # neuron h1
                self.w1 -= learning_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learning_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learning_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1
                # neuron h2
                self.w3 -= learning_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learning_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learning_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2
                # neuron o2
                self.w5 -= learning_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learning_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learning_rate * d_L_d_ypred * d_ypred_d_b3
            if (epoch % 10 == 0):
                y_preds = np.apply_along_axis(self.forwardPropagation, 1, data)
                loss = mseLoss(all_y_trues, y_preds)
                print("Epoch %d loss: %.3f" % (epoch, loss))
# training input
data = np.array([
    [6, -2],
    [18, 5],
    [-10, 3],
    [-11, -3]
])
# target
all_y_trues = np.array([1, 0, 0, 1])
# create object for initialization
nn = NeuralNetwork()
# train network
nn.train(data, all_y_trues)
# test sampe
p1 = np.array([-7, -3])
p2 = np.array([20, 5])
# result of test
print("P1: %.3f" % nn.forwardPropagation(p1))
print("P2: %.3f" % nn.forwardPropagation(p2))