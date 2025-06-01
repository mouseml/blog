import torch
from torch.nn import Sequential, Linear, ReLU, Sigmoid, Softmax

X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

model1 = Sequential(
    Linear(3, 16),
    ReLU(),
    Linear(16, 32),
    ReLU(),
    Linear(32, 5),
    Softmax(),
)
print(model1(X))

model2 = Sequential(
    Linear(3, 32),
    ReLU(),
    Linear(32, 32),
    ReLU(),
    Linear(32, 1),
)
print(model2(X))

model3 = Sequential(
    Linear(3, 16),
    ReLU(),
    Linear(16, 1),
    Sigmoid(),
)
print(model3(X))
