import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR problem)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Expected output
y = np.array([[0],
              [1],
              [1],
              [0]])

# Set seed for reproducibility
np.random.seed(42)

# Number of neurons
input_layer_neurons = 2
hidden_layer_neurons = 4
output_neurons = 1

# Weight and bias initialization
wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))  # weights from input to hidden
bh = np.random.uniform(size=(1, hidden_layer_neurons))                    # hidden layer bias

wo = np.random.uniform(size=(hidden_layer_neurons, output_neurons))      # weights from hidden to output
bo = np.random.uniform(size=(1, output_neurons))                          # output layer bias

# Training parameters
epochs = 10000
learning_rate = 0.1

# Training loop
for epoch in range(epochs):
    # Forward pass
    hidden_input = np.dot(X, wh) + bh
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, wo) + bo
    predicted_output = sigmoid(final_input)

    # Backpropagation
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden = d_predicted_output.dot(wo.T)
    d_hidden_layer = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights and biases
    wo += hidden_output.T.dot(d_predicted_output) * learning_rate
    bo += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    wh += X.T.dot(d_hidden_layer) * learning_rate
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# Final output
print("Final output after training:")
print(np.round(predicted_output, 3))
