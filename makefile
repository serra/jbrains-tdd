clean:
	rm -rf dist
	rm -rf build
	rm -rf serrajbrainstdd.egg-info
bootstrap:
	pip3 install pipenv --upgrade
	pipenv install
setup:
	pipenv shell
test:
	nosetests S01_fractions/tests --with-coverage
cibuild: test package
### Packageing and publishing
package:
	python setup.py sdist bdist_wheel
publish-to-test-pypi: clean package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
### bumpversion
bump-patch:
	bumpversion patch