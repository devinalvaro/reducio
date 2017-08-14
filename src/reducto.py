from articlesummarizer import ArticleSummarizer
from corpusreader import CorpusReader

corpus_type = input("What kind of article do you want to summarize? ")
corpus_reader = CorpusReader(corpus_type)

with open('data/article.txt', 'r') as file:
    article = file.read().replace('\n', ' ').replace('\r', '')

summary = ArticleSummarizer(article,
                            len(corpus_reader.articles),
                            corpus_reader.document_frequency)
