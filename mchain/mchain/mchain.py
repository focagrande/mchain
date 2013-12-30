# --*- coding: utf-8 -*-

import sys
import random
import string

class Mchain(object):
    "Class implements Markov Chain generator"

    def __init__(self):
        "Initializer"

        self.corpus_text = None
        self.degree = None
        self.maxwords = None


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

        for k in range(1, self.maxwords):
            
            try:
                posstate = self.core[tuple(self.mchain[len(self.mchain) - self.degree:])]
                nextword = posstate[random.randint(0, len(posstate) - 1)]
                self.mchain.append(nextword)
            except KeyError:
                None

        return string.join(self.mchain, ' ')

    def generate(self, corpus_text, degree, maxwords):
        "Generate Markov chain"

        self.corpus_text = corpus_text
        self.degree = degree
        self.maxwords = maxwords

        self._build_core()
        return self._build_mchain()

if __name__ == '__main__':

    try:
        cf = sys.argv[1]
        dg = int(sys.argv[2])
        mw = int(sys.argv[3])
    except IndexError:
        print "usage: %s corpus_file degree maxwords" % sys.argv[0]
        sys.exit(1)

    with open(cf, 'r') as f:
        ct = f.read()

    mc = Mchain()
    print mc.generate(ct, dg, mw)