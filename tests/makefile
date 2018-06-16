# This test verifies that we can install our package and use it.
# Runt it from this `tests` directory, in a clean virtual env.
test-package-installation:
	pip install --upgrade --no-cache-dir --index-url https://test.pypi.org/simple/ serrajbrainstdd
	python smoketest.py
	pip uninstall -y serrajbrainstdd