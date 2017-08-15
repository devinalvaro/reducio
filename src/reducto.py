from article_summarizer import ArticleSummarizer
from corpus_reader import CorpusReader

print("Please wait for the dataset to be processed...")

corpus_reader = CorpusReader()

with open('data/article.txt', 'r') as file:
    article = file.read().replace('\n', ' ').replace('\r', '')

summary = ArticleSummarizer(article, corpus_reader.document_number,
                            corpus_reader.document_frequency)

summary_percentage = float(
    input("To what percentage do you want to reducto the article? "))
top_sentences = summary.get_top_sentences(100 - summary_percentage)

print()
for top_sentence in top_sentences:
    print(top_sentence)
