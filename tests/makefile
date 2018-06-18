bootstrap:
	pip3 install pipenv --upgrade
	pipenv install
setup:
	pipenv shell
test-package-installation:
	pip install --upgrade --no-cache-dir --index-url https://test.pypi.org/simple/ serrajbrainstdd
	python smoketest.py
	pip uninstall -y serrajbrainstdd