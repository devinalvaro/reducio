from csv import DictReader

from tokenizer import tokenize_word


class CorpusReader:
    articles = []
    document_frequency = {}

    def __init__(self):
        self.filepath = 'data/news.csv'

        self.open_corpus()
        self.count_document_frequency()

    def open_corpus(self):
        with open(self.filepath, newline='', encoding='iso-8859-1') as csvfile:
            reader = DictReader(csvfile)
            for entry in reader:
                self.articles.append(entry['ctext'])

    def count_document_frequency(self):
        for article in self.articles:
            words = set(tokenize_word(article, only_noun=False))

            for word in words:
                if word not in self.document_frequency:
                    self.document_frequency[word] = 1
                else:
                    self.document_frequency[word] += 1
