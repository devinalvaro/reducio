from articlesummarizer import ArticleSummarizer
from corpusreader import CorpusReader

corpus_reader = CorpusReader()

with open('data/article.txt', 'r') as file:
    article = file.read().replace('\n', ' ').replace('\r', '')

summary = ArticleSummarizer(article,
                            len(corpus_reader.articles),
                            corpus_reader.document_frequency)

summary_percentage = float(
    input("To what percentage do you want to reducto the article? "))
top_sentences = summary.get_top_sentences(100 - summary_percentage)

print()
for top_sentence in top_sentences:
    print(top_sentence)
