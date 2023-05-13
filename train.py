import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words, tags, xy = [], [], []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        # We do not want an array of arrays so we extend it
        all_words.extend(w)
        # Pattern, tag
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

X_train, y_train = [], []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    # Cross entropy loss ; we only want the class labels
    y_train.append(label)

X_train, y_train = np.array(X_train), np.array(y_train)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
# Hyperparameters
# The first bag of words since they all have the same size
BATCH_SIZE, HIDDEN_SIZE, OUTPUT_SIZE, INPUT_SIZE, LEARNING_RATE, NUM_EPOCHS = 8, 8, len(tags), len(X_train[0]), 0.001, 1000

dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset, batch_size = BATCH_SIZE, shuffle = True, num_workers = 2)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = LEARNING_RATE)

for epoch in range(NUM_EPOCHS):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        # Forward
        outputs = model(words)
        