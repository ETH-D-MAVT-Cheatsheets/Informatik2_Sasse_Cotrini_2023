from sklearn.neural_network import MLPRegressor
#hidden_layer_sizes: array indicating number of neurons per layer
#activation: activation function
model = MLPRegressor(hidden_layer_sizes = [4,4], activation="relu")
