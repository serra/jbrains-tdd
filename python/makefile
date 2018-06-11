# this makefile assumes we are in a (virtual) env with python 3.6
bootstrap:
	pip install -r requirements.txt
test:
	nosetests tests
cibuild:
	python setup.py sdist bdist_wheel