import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

FILE = "data.pth"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as f:
    intents = json.load(f)

data = torch.load(FILE)
INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE, ALL_WORDS, TAGS, MODEL_STATE, BOT_NAME = data["input_size"], data["hidden_size"], data["output_size"], data["all_words"], data["tags"], data["model_state"], "Benbot"
model = NeuralNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE).to(device)
# Knows our learned parameters
model.load_state_dict(MODEL_STATE)
model.eval()
print("Let's chat! Type 'quit' to exit ...")

while True:
    sentence = input('You: ')

    if sentence == 'quit':
        break

    sentence = tokenize(sentence)
    # Numpy array
    X = bag_of_words(sentence, ALL_WORDS)
    # Single row, single column
    X = X.reshape(1, X.shape[0])
    # Convert to a torch tensor
    X = torch.from_numpy()
    
    output = model(X)
    _, predicted = torch.max(output, dim = 1)
    # predicted.item() is the class label
    # tag will be the tag that we store such as 'greeting'
    tag = TAGS[predicted.item()]