words = [i.strip().lower() for i in open('/usr/share/dict/words').readlines()]
tlds = [i.split()[0].strip().lower() for i in open('tlds.txt').readlines()]

for word in words:
  for tld in tlds:
    if word.endswith(tld):
      print '%s.%s' % (word.rstrip(tld), tld)