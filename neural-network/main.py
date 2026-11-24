import numpy as np

# data
X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
y = np.array([[0], [0], [1], [1]])

# network of 2 input, 2 hidden & 1 output
# random numbers
rng = np.random.default_rng(1)
# hidden weights
W1 = rng.normal(size=(2, 2))
# output weights
W2 = rng.normal(size=(2, 1))
# hidden bias
b1 = np.zeros(2)
# output bias
b2 = np.zeros(1)

# activation functions
# relu function return positive if input is not 0
def relu(z):
    return np.maximum(0, z)

# sigmoid function
# output value always falls between (0, 1)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# training learning rate to determine speed of pursuit
lr = 1.0
print(" Step    Loss")
for step in range(1, 1501):
    # forward propagation (matrix multiplication)
    # hidden layer
    h = relu(X @ W1 + b1)
    # prediction
    y_hat = sigmoid(h @ W2 + b2)

    # loss tell how wrong the model is
    loss = -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

    # back propagation
    d2 = (y_hat - y) / 4
    d1 = (d2 @ W2.T) * (h > 0)

    # update the weights and bias
    W1 -= lr * (X.T @ d1)
    b1 -= lr * d1.sum(axis = 0)
    W2 -= lr * (h.T @ d2)
    b2 -= lr * d2.sum(axis = 0)

    if (step == 1 or step % 150 == 0):
        print(f"{step: 4d}  {loss: .3f}")

# final result
print(f"\n{y_hat.round(2)}")