#!/usr/bin/env python

import sys
from random import choice
import argparse

def parse_arguments():
    ''' parse the arguments '''

    p = argparse.ArgumentParser()

    p.add_argument('--words-file',
                   help='file with list of words [/usr/share/dict/words]',
                   default='/usr/share/dict/words')

    p.add_argument('--tlds-file',
                   help='file with list of tlds [tlds.txt]',
                   default='tlds.txt')

    p.add_argument('--tlds',
                   help='manually specify tlds as comma-separated list',
                   default=False)

    return p.parse_args()


def get_words(words_file, min_length=1):
    ''' iterate over list of words in text file '''

    words = []

    with open(words_file) as handle:
        for word in handle:
            word = word.strip().lower()
            if len(word) > min_length:
                words.append(word)

    return words


def get_tlds(tlds_file):
    ''' iterate over list of tlds in text file '''

    tlds = []

    with open(tlds_file) as handle:
        for tld in handle:
            tld = tld.split()[0].strip().lower()
            tlds.append(tld)

    return tlds


def get_domains(words, tlds):
    ''' list domains made from words and tlds '''

    for word in words:
        for tld in tlds:
            if word.endswith(tld):
                yield '%s.%s' % (word.rstrip(tld), tld)


if __name__ == '__main__':
    args = parse_arguments()

    words = get_words(args.words_file)

    if not args.tlds:
        tlds = get_tlds(args.tlds_file)
    else:
        tlds = args.tlds.split(',')

    for domain in get_domains(words, tlds):
        print domain
