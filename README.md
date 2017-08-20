# Reducio

Reducio is a program that summarizes text with [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term frequency - inverse document frequency) weighting scheme.

This project was initially started as an assignment from Artificial Intelligence and Graphics Laboratory, Institut Teknologi Bandung.

### How It Works
In a nutshell, here's how Reducio summarizes a news article:

1. Tokenize the article into words and sentences.
2. Score each word with tf-idf (explained below).
3. Score each sentence by the average score of its words.
4. Display top n sentences as the summary.

#### Tf-idf

[tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term frequency-inverse document frequency) is a numerical statistics that values each word in a text according to its importance in the text.

A word is considered more important if it appears more frequently in the text (term frequency). However, its importance decreases as it appears more often in other texts (inverse document frequency).

Because of this, Reducio pre-processes a large [dataset of news](https://www.kaggle.com/patjob/articlescrape) to provide better results for the idf part.

### Prerequisites

1. python3
   - **Linux**: https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python
   - **Windows**: https://docs.python.org/3/using/windows.html#installing-python
   - **Mac**: https://docs.python.org/3/using/mac.html#getting-and-installing-macpython

2. pip3

   https://pip.pypa.io/en/stable/installing/

### Usage

1. `git clone https://github.com/devinalvaro/reducio`
2. `cd reducio`
3. `make`
4. `python3 src/reducio.py`

### License

This project is licensed under the MIT License - see the LICENSE file for details
