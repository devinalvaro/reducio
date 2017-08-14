from corpusreader import CorpusReader
from articlesummarizer import ArticleSummarizer

corpus_type = input("What kind of article do you want to summarize? ")
corpus_reader = CorpusReader(corpus_type)

article = input("Please put the article here:\n")
summary = ArticleSummarizer(article,
                            len(corpus_reader.articles),
                            corpus_reader.document_frequency)
