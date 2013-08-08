import sys
from random import choice
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--words_file', help='file with list of words', default='/usr/share/dict/words')
    parser.add_argument('--tlds_file', help='file with list of tlds', default='tlds.txt')
    return parser.parse_args()


def words(words_file):
    ''' iterate over list of words in text file '''
    with open(words_file) as handle:
        for word in handle:
            yield word.strip().lower()


def tlds(tlds_file):
    ''' iterate over list of tlds in text file '''
    with open(tlds_file) as handle:
        for tld in handle:
            yield tld.split()[0].strip().lower()

def get_domains(words_file, tlds_file):
    for word in words(words_file):
        for tld in tlds(tlds_file):
          if word.endswith(tld):
              yield '%s.%s' % (word.rstrip(tld), tld)


if __name__ == '__main__':
    args = parse_arguments()

    for domain in get_domains(args.words_file, args.tlds_file):
        print domain
