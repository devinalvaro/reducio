from json import dump

from src.article_summarizer import ArticleSummarizer
from src.corpus_reader import CorpusReader


def reducio(sentence_number=5):
    corpus_reader = CorpusReader()

    with open('data/article.txt', 'r') as file:
        article = file.read().replace('\n', ' ').replace('\r', '')

    summary = ArticleSummarizer(article, corpus_reader.document_number,
                                corpus_reader.document_frequency)

    top_sentences = summary.get_top_sentences(sentence_number)

    top_sentences = dict(enumerate(top_sentences, 1))
    with open('data/sentences.json', 'w') as jsonfile:
        dump(top_sentences, jsonfile)
