#!/usr/bin/env python3

import sys
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
                    action='store_true')

    p.add_argument('--min-size', default=0, type=int, help='minimum word length')
    p.add_argument('--max-size', default=100000, type=int, help='maximum word length')

    return p.parse_args()


def iter_words(handle):
    ''' iterate over list of words in text file '''

    return (
        word.strip().lower()
        for word
        in handle
    )


def get_tlds(tlds_file):
    ''' iterate over list of tlds in text file '''

    with open(tlds_file) as handle:

        return [
            line.split()[0].strip().lower()
            for line in handle
        ]

def iter_domains(words, tlds):
    ''' list domains made from words and tlds '''

    return (
        '{}.{}'.format(word.rstrip(tld), tld)
        for word in words
        for tld in tlds
        if word.endswith(tld)
    )


def l33tify(domain):
    ''' Produce 1337 versions of words '''

    replacements = {
      'a': '4',
      'b': '8',
      'e': '3',
      'g': '6',
      'i': '1',
      'o': '0',
      's': '5',
      't': '7',
      'z': '2'
    }

    word, tld = domain.split('.')

    return ''.join([
        replacements.get(char, char)
        for char
        in word
    ]) + '.' + tld


if __name__ == '__main__':
    args = parse_arguments()

    if not args.tlds:
        tlds = get_tlds(args.tlds_file)
    else:
        tlds = args.tlds.split(',')

    with open(args.words_file) as handle:
        processed_domains = (
            l33tify(domain) if args.leet else domain
            for domain
            in iter_domains(iter_words(handle), tlds)
            if len(domain) in range(args.min_size, args.max_size)
        )

        for domain in processed_domains:
            print(domain)
