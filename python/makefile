clean:
	rm -rf dist
	rm -rf build
bootstrap:
	pipenv install
setup:
	pipenv shell
test:
	nosetests tests
cibuild: package
### Packageing and publishing
package:
	python setup.py sdist bdist_wheel
publish-to-test-pypi: clean package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
### bumpversion
bump-patch:
	bumpversion patch