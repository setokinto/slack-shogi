
from setuptools import setup, find_packages

setup(
    name="Slack Shogi Emoji Importer",
    version="0.1",
    packages=find_packages(),
    test_suite="test",
    install_requires=[
        "mechanize",
        "requests",
        "beautifulsoup4",
        "lxml",
    ],
)
