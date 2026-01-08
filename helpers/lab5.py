import numpy as np

class SimplePerceptron:
    def __init__(self, alpha=0.1):
        self.w1 = 0
        self.w2 = 0
        self.b = 0
        self.alpha = alpha

    def forward(self, x):
        y = self.w1 * x[0] + self.w2 * x[1] + self.b
        return 1 / (1 + np.exp(-y))

    def loss(self, y_pred, y):
        return -y * np.log(y_pred) - (1 - y) * np.log(1 - y_pred)

    @staticmethod
    def get_grad_w1(x, y_pred, y_true):
        return (y_pred - y_true) * x[0]

    @staticmethod
    def get_grad_w2(x, y_pred, y_true):
        return (y_pred - y_true) * x[1]

    @staticmethod
    def get_grad_b(y_pred, y_true):
        return y_pred - y_true

    def update(self, x, y_pred, y_true):
        self.w1 -= self.alpha * self.get_grad_w1(x, y_pred, y_true)
        self.w2 -= self.alpha * self.get_grad_w2(x, y_pred, y_true)
        self.b -= self.alpha * self.get_grad_b(y_pred, y_true)

def plot_gradient_descent(f, xs):
    import matplotlib.pyplot as plt
    import seaborn as sns

    x_range = np.linspace(-2, 2, 100)
    y = f(x_range)

    sns.set_style('whitegrid')
    sns.set_context('talk')

    plt.plot(x_range, y)
    plt.title('Gradient Descent')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(xs, [f(x) for x in xs], c='crimson', marker='o')


import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, hidden_size):
        super(NeuralNetwork, self).__init__()
        self.hidden = nn.Linear(1, hidden_size)  # hidden layer
        self.output = nn.Linear(hidden_size, 1)  # output layer
        self.relu = nn.ReLU()  # ReLU activation function

    def forward(self, x):
        h = self.hidden(x)  # pass the input through the hidden layer
        h = self.relu(h)  # apply ReLU activation function
        y = self.output(h)  # pass the result through the output layer
        return y