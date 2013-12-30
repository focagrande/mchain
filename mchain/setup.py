# --*- coding: utf-8 -*-

import os
from setuptools import setup

setup(
    name = "mchain",
    version = "0.0.1",
    author = "Jacek Śpiewak",
    author_email = "jacek.spiewak@gmail.com",
    description = ("Human readable text generator based on Markov chains"),
    keywords = "markov chain text generator",
    url = "http://focagrande.github.io",
    packages=['mchain'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities"
    ],
)