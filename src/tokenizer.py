import re

from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize


def tokenize_word(text, only_noun):
    """ Tokenize a text into words using NLTK

    Filter punctuation (non-alphanumeric characters).
    Filter stop words.
    Filter non-noun words, if only_noun=true

    Args:
        text: Text to be tokenized into words.
        only_noun: A boolean, if true then filter non-noun words
    Returns:
        A list of word tokens.
    """

    text = text.lower()

    pattern = re.compile(r'[^a-zA-Z\s]')
    text = pattern.sub(' ', text)

    word_tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    word_tokens = [word for word in word_tokens if word not in stop_words]

    if only_noun:
        word_tokens = pos_tag(word_tokens)
        word_tokens = [word for (word, tag) in word_tokens if 'NN' in tag]

    return word_tokens


def tokenize_sentence(text):
    """Tokenize a text into sentences using NLTK

    Args:
        text: Text to be tokenized into sentences.
    """

    sentence_tokens = sent_tokenize(text)

    return sentence_tokens
