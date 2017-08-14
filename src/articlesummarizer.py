from tfidf import term_frequency as tf, inverse_document_frequency as idf
from tokenizer import tokenize_word, tokenize_sentence


class ArticleSummarizer:
    sentence_scores = []
    word_frequency = {}

    def __init__(self, article, document_number, document_frequency):
        self.article = article
        self.document_number = document_number
        self.document_frequency = document_frequency

        words = tokenize_word(self.article)
        for word in words:
            if word not in self.word_frequency:
                self.word_frequency[word] = 1
            else:
                self.word_frequency[word] += 1

        self.sentences = tokenize_sentence(self.article)
        for sentence in self.sentences:
            self.sentence_scores.append(self.sentence_score(sentence))

    def sentence_score(self, sentence):
        words = tokenize_word(sentence)

        total = 0
        for word in words:
            total += self.word_score(word)

        return total / len(words)

    def word_score(self, word):
        return tf(word, self.word_frequency) * idf(word, self.document_number,
                                                   self.document_frequency)
