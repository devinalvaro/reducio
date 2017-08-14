from operator import itemgetter

from tf_idf import term_frequency as tf, inverse_document_frequency as idf
from tokenizer import tokenize_word, tokenize_sentence


class ArticleSummarizer:
    sentence_scores = []
    word_frequency = {}

    def __init__(self, article, document_number, document_frequency):
        self.article = article
        self.document_number = document_number + 1
        self.document_frequency = document_frequency

        words = tokenize_word(self.article)
        for word in words:
            if word not in self.word_frequency:
                self.word_frequency[word] = 1
            else:
                self.word_frequency[word] += 1

        words = set(words)
        for word in words:
            if word not in self.document_frequency:
                self.document_frequency[word] = 1
            else:
                self.document_frequency[word] += 1

        self.sentences = tokenize_sentence(self.article)
        for sentence in self.sentences:
            self.sentence_scores.append((self.sentence_score(sentence),
                                         sentence))

        self.sentence_scores = sorted(
            self.sentence_scores, key=itemgetter(0), reverse=True)

        self.top_sentences = [sentence[1] for sentence in self.sentence_scores]

    def sentence_score(self, sentence):
        words = tokenize_word(sentence)

        if not words:
            return 0

        total = 0
        for word in words:
            total += self.word_score(word)

        return total / len(words)

    def word_score(self, word):
        return tf(word, self.word_frequency) * idf(word, self.document_number,
                                                   self.document_frequency)

    def get_top_sentences(self, percentage):
        n = int(percentage / 100 * len(self.sentences))

        top_n_sentences = [
            sentence for sentence in self.sentences
            if sentence in self.top_sentences[0:n]
        ]

        return top_n_sentences
