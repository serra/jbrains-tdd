# This test verifies that we can install our package and use it.
# Runt it from this `tests` directory, in a clean virtual env.
test-package-installation:
	pip install --index-url https://test.pypi.org/simple/ serrajbrainstdd
	python packaging.py
	pip uninstall -y serrajbrainstdd