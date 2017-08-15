from json import dump, load
from pandas import read_csv

from tokenizer import tokenize_word


class CorpusReader:
    """Corpus reader

    Try to open JSON file containing document number and document frequency.
    If fails, open corpus dataset and count the document frequency of each word.
    """

    __articles = []
    document_frequency = {}

    def __init__(self):
        """Inits CorpusReader

        Try to open JSON file containing document number and frequency.

        If it fails, open corpus dataset.
        Count the document frequency of each word.
        """

        try:
            with open('data/news.json', 'r') as jsonfile:
                cache = load(jsonfile)

                self.document_number = cache[0]
                self.document_frequency = cache[1]
        except IOError:
            with open('data/news.json', 'w') as jsonfile:
                self.__open_corpus()
                self.__count_document_frequency()

                self.document_number = len(self.__articles)

                dump((self.document_number, self.document_frequency), jsonfile)

    def __open_corpus(self):
        # open corpus dataset and store it in self.__articles

        with open('data/news.csv') as csvfile:
            reader = read_csv(csvfile)
            for entry in reader['body']:
                self.__articles.append(str(entry))

    def __count_document_frequency(self):
        # count the document frequency of each word

        count = 0
        for article in self.__articles:
            count += 1
            if count % 1000 == 0:
                print(count)

            words = set(tokenize_word(article, only_noun=False))
            for word in words:
                if word not in self.document_frequency:
                    self.document_frequency[word] = 1
                else:
                    self.document_frequency[word] += 1
