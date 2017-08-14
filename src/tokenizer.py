import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def tokenize_word(text):
    # lowercase text
    text = text.lower()

    # filter punctuation
    pattern = re.compile('[^A-Za-z -]+')
    text = pattern.sub('', text)

    # tokenize text into words
    word_tokens = word_tokenize(text)

    # filter stop words
    stop_words = set(stopwords.words('english'))
    word_tokens = [word for word in word_tokens if word not in stop_words]

    return word_tokens


def tokenize_sentence(text):
    # tokenize text into sentences
    sentence_tokens = sent_tokenize(text)

    return sentence_tokens
