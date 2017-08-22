#!/usr/bin/env python

import sys
from random import choice
from itertools import product
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

    p.add_argument('--leet',
                    help='generate domains that replace letters with numbers',
                    action="store_true")

    p.add_argument('--min-three-chars',
                    help='three characters minimum, ex: 123.tld',
                    dest="three",
                    action="store_true")

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

        return [
            line.split()[0].strip().lower()
            for line in handle
        ]



def get_domains(words, tlds):
    ''' list domains made from words and tlds '''

    for word in words:
        for tld in tlds:
            if word.endswith(tld):
                yield '%s.%s' % (word.rstrip(tld), tld)



def generate_leet_versions(words):
    ''' Produce 1337 versions of words '''
    leet_words = []

    replacements = {'a': '4', 'b': '8', 'e': '3', 'g': '6', 'i': '1', 'o': '0', 's': '5', 't': '7', 'z': '2'}

    ''' replace all '''
    for word in words:
        leet_words.append(word)
        leet_versions = set()
        letter_options = []
        for letter in word:
            if letter in replacements:
                replacement = replacements[letter]
                letter_options.append( (letter,replacement) )
            else:
                letter_options.append( (letter,) )
        for letters_in_leet_version in product(*letter_options):
            a_leet_word = ''.join(letters_in_leet_version)
            if a_leet_word != word:
                leet_versions.add(a_leet_word)
        for leet_version in list(leet_versions):
            leet_words.append(leet_version)

    return leet_words



if __name__ == '__main__':
    args = parse_arguments()

    words = get_words(args.words_file)

    if args.leet:
        words = generate_leet_versions(words)

    if not args.tlds:
        tlds = get_tlds(args.tlds_file)
    else:
        tlds = args.tlds.split(',')

    for domain in get_domains(words, tlds):
        if args.three:
            if len( domain[:domain.find('.')] ) >= 3:
                print domain
        else:
            print domain
