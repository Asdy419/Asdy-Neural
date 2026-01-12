import numpy as np

class HiddenLayer:
    def __init__(self, input, activation):
        self.activation = activation
        self.input = input
        self.weight = weight
    
    def get_weight(self):
        ...
    
    def set_weight(self):
        ...
    

"""
hidden_layer_data = {
    'activation_type' : "..."
    'layers_data' : {'Layer1' : shape, 'Layer2' : shape, 'Layer3' : shape .... 'LayerN' : shape} 
    }
"""

"""
output_layer_data = {
    'activation_type' : "..."
    'neurons' : N
    }
"""

"""
input_layer_data = {
    'input_data' : "..."
    'backprop_shape' : {NxM} <- vector / matrix of batch 
}
"""

class Network:
    def __init__(self, input_layer_data, hidden_layer_data, output_layer_data, lr, epochs):
        ...        
