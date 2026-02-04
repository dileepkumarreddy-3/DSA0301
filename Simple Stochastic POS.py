import random

words = ["I", "run", "a", "race"]

pos_probabilities = {
    "I": {"PRP": 1.0},
    "run": {"VB": 0.6, "NN": 0.4},
    "a": {"DT": 1.0},
    "race": {"NN": 0.7, "VB": 0.3}
}

tagged_sentence = []

for w in words:
    tags = list(pos_probabilities[w].keys())
    probs = list(pos_probabilities[w].values())
    tag = random.choices(tags, probs)[0]
    tagged_sentence.append((w, tag))

for item in tagged_sentence:
    print(item)
