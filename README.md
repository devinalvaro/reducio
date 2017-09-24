# Reducio

Reducio is a program that summarizes text with [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term frequency - inverse document frequency) weighting scheme. See it in action at <https://reducio.herokuapp.com>.

This project was initially started as an assignment from Artificial Intelligence and Graphics Laboratory, Institut Teknologi Bandung.

### How It Works

In a nutshell, here's how Reducio summarizes a news article:

1. Tokenize the article into words and sentences.
2. Score each word with tf-idf (explained below).
3. Score each sentence by the average score of its words.
4. Display top n sentences as the summary.

#### Tf-idf

[Tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term frequency-inverse document frequency) is a numerical statistics that values each word in a text according to its importance in the text.

A word is considered more important if it appears more frequently in the text (term frequency). However, its importance decreases as it appears more often in other texts (inverse document frequency).

Idf works better the more texts there are in the dataset. Because of this, Reducio pre-processes a large [dataset of news](https://www.kaggle.com/patjob/articlescrape) to provide better results for the idf part.

### Usage

Simply visit <https://reducio.herokuapp.com>.

### Documentation

To generate the project's documentation:

1. Run `pip install sphinx`
2. Run `make html` from `doc` directory.

Open the documentation with browser at `doc/build/html/index.html`.

### Built with

- Languages: Python 3, JavaScript, HTML, CSS
- Libraries: [NLTK](http://www.nltk.org), [Pandas](http://pandas.pydata.org), [jQuery](https://jquery.com)
- Web Frameworks: [Flask](http://flask.pocoo.org), [Bootstrap](http://getbootstrap.com)
- Documentation: [Sphinx](http://www.sphinx-doc.org)

### License

This project is licensed under the MIT License - see the LICENSE file for details
