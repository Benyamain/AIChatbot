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

def get_response(message):
    sentence = tokenize(message)
    # Numpy array
    X = bag_of_words(sentence, ALL_WORDS)
    # Single row, single column
    X = X.reshape(1, X.shape[0])
    # Convert to a torch tensor
    X = torch.from_numpy(X)
    
    output = model(X)
    _, predicted = torch.max(output, dim = 1)
    # predicted.item() is the class label
    # tag will be the tag that we store such as 'greeting'
    tag = TAGS[predicted.item()]

    # Check if probability for tag is high enough using softmax
    probability = torch.softmax(output, dim = 1)
    actual_probability_for_tag = probability[0][predicted.item()]

    if actual_probability_for_tag.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
            
    return "I do not understand ..."