from articlesummarizer import ArticleSummarizer
from corpusreader import CorpusReader

corpus_type = input("What kind of article do you want to reducto/summarize? ")
corpus_reader = CorpusReader(corpus_type)

print()

with open('data/article.txt', 'r') as file:
    article = file.read().replace('\n', ' ').replace('\r', '')

summary = ArticleSummarizer(article,
                            len(corpus_reader.articles),
                            corpus_reader.document_frequency)

summary_percentage = float(
    input("To what percentage do you want to reducto the article? "))

print()

top_sentences = summary.get_top_sentences(100 - summary_percentage)
for top_sentence in top_sentences:
    print(top_sentence)
