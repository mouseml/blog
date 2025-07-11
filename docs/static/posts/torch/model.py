import torch

def relu(x):
    return torch.maximum(x, torch.zeros_like(x))

X_train = torch.load("X_train.pt")
y_train = torch.load("y_train.pt")
X_val = torch.load("X_val.pt")
y_val = torch.load("y_val.pt")

W1 = torch.randn(11, 64, requires_grad=True)
b1 = torch.randn(64, requires_grad=True)
W2 = torch.randn(64, 1, requires_grad=True)
b2 = torch.randn(1, requires_grad=True)

alpha = 0.01

for _ in range(1000):
    y_hat = relu(X_train @ W1 + b1) @ W2 + b2
    loss = ((y_hat - y_train) ** 2).mean()
    loss.backward()
    with torch.no_grad():
        W1 -= alpha * W1.grad
        b1 -= alpha * b1.grad
        W2 -= alpha * W2.grad
        b2 -= alpha * b2.grad
    W1.grad = None
    b1.grad = None
    W2.grad = None
    b2.grad = None

with torch.no_grad():
    y_hat = relu(X_val @ W1 + b1) @ W2 + b2
score = (y_hat - y_val).abs().mean()
print(f"Среднее отклонение: {score:.2f} балла.")
