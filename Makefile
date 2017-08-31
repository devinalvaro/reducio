init:
	pip2 install --user -r prerequisites/py2_requirements.txt
	pip3 install --user -r prerequisites/py3_requirements.txt
	python3 prerequisites/nltk_dl.py
