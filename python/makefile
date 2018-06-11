# this makefile assumes we are in a (virtual) env with python 3.6
bootstrap:
	pip install -r requirements.txt
test:
	nosetests tests
cibuild: package
package:
	python setup.py sdist bdist_wheel
publish-to-test-pypi: package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*