from operator import itemgetter

from tf_idf import term_frequency as tf, inverse_document_frequency as idf
from tokenizer import tokenize_word, tokenize_sentence


class ArticleSummarizer:
    sentence_scores = []
    word_frequency = {}

    def __init__(self, article, document_number, document_frequency):
        self.sentences = tokenize_sentence(article)
        self.document_number = document_number + 1
        self.document_frequency = document_frequency

        word_set = set()

        for sentence in self.sentences:
            words = tokenize_word(sentence, only_noun=True)
            for word in words:
                if word not in self.word_frequency:
                    self.word_frequency[word] = 1
                else:
                    self.word_frequency[word] += 1

                word_set.add(word)

        for word in word_set:
            if word not in self.document_frequency:
                self.document_frequency[word] = 1
            else:
                self.document_frequency[word] += 1

        for sentence in self.sentences:
            self.sentence_scores.append(
                [self.sentence_score(sentence), sentence])

        self.weigh_sentences_by_position()

        self.sentence_scores = sorted(
            self.sentence_scores, key=itemgetter(0), reverse=True)
        self.ranked_sentences = [
            sentence[1] for sentence in self.sentence_scores
        ]

    def sentence_score(self, sentence):
        words = tokenize_word(sentence, only_noun=True)

        if not words:
            return 0

        total = 0
        for word in words:
            total += self.word_score(word)

        return total / len(words)

    def word_score(self, word):
        return tf(word, self.word_frequency) * idf(word, self.document_number,
                                                   self.document_frequency)

    def weigh_sentences_by_position(self):
        for index, sentence_score in enumerate(self.sentence_scores):
            distribution = index / len(self.sentence_scores)

            if 0 <= distribution and distribution < 0.1:
                weight = 0.17
            elif 0.1 <= distribution and distribution < 0.2:
                weight = 0.23
            elif 0.2 <= distribution and distribution < 0.3:
                weight = 0.14
            elif 0.3 <= distribution and distribution < 0.4:
                weight = 0.08
            elif 0.4 <= distribution and distribution < 0.5:
                weight = 0.05
            elif 0.5 <= distribution and distribution < 0.6:
                weight = 0.04
            elif 0.6 <= distribution and distribution < 0.7:
                weight = 0.06
            elif 0.7 <= distribution and distribution < 0.8:
                weight = 0.04
            elif 0.8 <= distribution and distribution < 0.9:
                weight = 0.04
            else:
                weight = 0.15

            sentence_score[0] *= weight

    def get_top_sentences(self, percentage):
        n = int(percentage / 100 * len(self.sentences))
        top_n_sentences = [
            sentence for sentence in self.sentences
            if sentence in self.ranked_sentences[0:n]
        ]

        return top_n_sentences
