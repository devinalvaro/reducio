from json import dump, load
from pandas import read_csv

from tokenizer import tokenize_word


class CorpusReader:
    """Corpus reader

    Open corpus dataset and count the document frequency of each word.
    """

    articles = []
    document_frequency = {}

    def __init__(self):
        """Inits CorpusReader

        Open corpus dataset.
        Count the document frequency of each word.
        """

        try:
            with open('data/news.json', 'r') as jsonfile:
                cache = load(jsonfile)

                self.document_number = cache[0]
                self.document_frequency = cache[1]
        except IOError:
            with open('data/news.json', 'w') as jsonfile:
                self.open_corpus()
                self.count_document_frequency()

                self.document_number = len(self.articles)

                dump((self.document_number, self.document_frequency), jsonfile)

    def open_corpus(self):
        """Open corpus dataset and store it in self.articles"""

        with open('data/news.csv') as csvfile:
            reader = read_csv(csvfile)
            for entry in reader['ctext']:
                self.articles.append(str(entry))

    def count_document_frequency(self):
        """Count the document frequency of each word"""

        for article in self.articles:
            words = set(tokenize_word(article, only_noun=False))
            for word in words:
                if word not in self.document_frequency:
                    self.document_frequency[word] = 1
                else:
                    self.document_frequency[word] += 1
