import sys
from random import choice

class DomainGetter:

  def __init__(self):
    self.words = [i.strip().lower() for i in open('/usr/share/dict/words').readlines()]
    self.tlds = [i.split()[0].strip().lower() for i in open('tlds.txt').readlines()]

  def __iter__(self):
    while len(self.words) > 1:

      word = choice(self.words)
      self.words.remove(word)

      for tld in self.tlds:
        if word.endswith(tld):
          yield '%s.%s' % (word.rstrip(tld), tld)
        else:
          yield False


domains = DomainGetter()

for domain in domains:
  if domain:
    print domain
