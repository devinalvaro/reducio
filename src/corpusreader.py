import csv

from tokenizer import tokenize_word


class CorpusReader:
    articles = []
    words = {}

    def __init__(self, corpustype):
        if corpustype == 'news':
            self.filepath = '../data/news.csv'

        self.open_corpus()
        self.count_words()

    def open_corpus(self):
        with open(self.filepath, newline='', encoding='iso-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for entry in reader:
                self.articles.append(entry['ctext'])

    def count_words(self):
        for article in self.articles:
            word_tokens = set(tokenize_word(article))

            for word in word_tokens:
                if word not in self.words:
                    self.words[word] = 1
                else:
                    self.words[word] += 1
