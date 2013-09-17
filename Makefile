heroku: hello/templates/hello/README.html
	git push -f heroku master

hello/templates/hello/README.html: README.rst
	rst2html.py README.rst > hello/templates/hello/README.html
