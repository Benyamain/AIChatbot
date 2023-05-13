import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

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
print(tags)

X_train, y_train = [], []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    # Cross entropy loss ; we only want the class labels
    y_train.append(label)

X_train, y_train = np.array(X_train), np.array(y_train)