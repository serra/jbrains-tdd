from setuptools import setup
from setuptools import find_packages

__version__ = '0.1.0'

setup(
    name='serrajbrainstdd',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],

    # metadata for upload to PyPI
    author="Marijn van der Zee",
    author_email="marijn@serraict.com",
    description="Generate a static site from a Github wiki",
    license="GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007",
    keywords="",
    url="https://www.serraict.com",
)
