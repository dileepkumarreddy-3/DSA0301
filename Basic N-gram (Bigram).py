import random

text = "i like machine learning and i like python"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    pair = (words[i], words[i + 1])
    if pair[0] not in bigrams:
        bigrams[pair[0]] = []
    bigrams[pair[0]].append(pair[1])

word = random.choice(words)
generated = [word]

for i in range(10):
    if word in bigrams:
        word = random.choice(bigrams[word])
        generated.append(word)
    else:
        break

print(" ".join(generated))
