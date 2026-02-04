import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

words = ["running", "better", "cars", "feet"]

for w in words:
    print(w, "->", lemmatizer.lemmatize(w))
