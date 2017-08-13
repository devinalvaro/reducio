import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Tokenizer:
    def __init__(self, text):
        self.text = text

    def word_tokenize(self):
        # lowercase text
        self.text = self.text.lower()

        # filter punctuation
        pattern = re.compile('[^A-Za-z -]+')
        self.text = pattern.sub('', self.text)

        # tokenize text into words
        word_tokens = word_tokenize(self.text)

        # filter stop words
        stop_words = set(stopwords.words('english'))
        word_tokens = [word for word in word_tokens if word not in stop_words]

        return word_tokens
