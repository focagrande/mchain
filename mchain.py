# --*- coding: utf-8 -*-

import random
import string

class Mchain(object):
    "Class implements Markov Chain generator"

    def __init__(self, corpus_text, degree):
        "Initializer"

        self.corpus_text = corpus_text
        self.degree = degree
        self.corpus = []
        self.core = {}
        self.mchain = []

    def _build_core(self):
        "Create corpus"

        self.corpus = self.corpus_text.split()

        for k in range(len(self.corpus) - self.degree):

            key = tuple(self.corpus[k:k + self.degree])

            if not key in self.core:
                self.core[key] = []

            self.core[key].append(self.corpus[k + self.degree])

    def _build_mchain(self):
        "Generate Markov chain"

        self.mchain = self.corpus[:self.degree]

        for k in range(1, 100):
            
            try:
                posstate = self.core[tuple(self.mchain[len(self.mchain) - self.degree:])]
                nextword = posstate[random.randint(0, len(posstate) - 1)]
                self.mchain.append(nextword)
            except KeyError:
                None

        return string.join(self.mchain, ' ')

    def generate(self):
        "Generate Markov chain"
        self._build_core()
        return self._build_mchain()

