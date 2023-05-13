import torch
import torch.nn as nn

class NeuralNet(nn.Module):

    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.linear_1 = nn.Linear(input_size, hidden_size)
        self.linear_2 = nn.Linear(hidden_size, hidden_size)
        self.linear_3 = nn.Linear(hidden_size, num_classes)
        # Activation function
        self.relu = nn.ReLU()

    def forward(self, x):
        output = self.linear_1(x)
        output = self.relu(output)
        output = self.linear_2(output)
        output = self.relu(output)
        output = self.linear_3(output)
        # No activation and no softmax since cross entropy will do that for us
        return output