# --*- coding: utf-8 -*-

from mchain import Mchain

def main(ct, dg):
    mc = Mchain(ct, dg)
    return mc.generate()

if __name__ == '__main__':

    corpus_fname = './corpus/corpus_5.txt'

    with open(corpus_fname, 'r') as f:
        corpus_txt = f.read()

    print main(corpus_txt, 1)
    print '----------------------------------------------------'
    print main(corpus_txt, 2)