from src.article_summarizer import ArticleSummarizer
from src.corpus_reader import CorpusReader


def reducio(sentence_number=5):
    corpus_reader = CorpusReader()

    with open('data/article.txt', 'r') as file:
        article = file.read().replace('\n', ' ').replace('\r', '')

    summary = ArticleSummarizer(article, corpus_reader.document_number,
                                corpus_reader.document_frequency)

    top_sentences = summary.get_top_sentences(sentence_number)

    summarized_article = ''
    for sentence in top_sentences:
        summarized_article += (sentence + '<br />')

    return summarized_article
