from math import log10


def term_frequency(word, word_frequency):
    return 0 if word_frequency[word] == 0 else 1 + log10(word_frequency[word])


def inverse_document_frequency(word, document_number, document_frequency):
    return log10(document_number / document_frequency[word])
