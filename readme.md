# Clever Domain Name Generator

Generates domains where the TLD forms part of a word.


```
usage: tld.py [-h] [--words-file WORDS_FILE] [--tlds-file TLDS_FILE]
              [--tlds TLDS] [--leet] [--min-size MIN_SIZE]
              [--max-size MAX_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --words-file WORDS_FILE
                        file with list of words [/usr/share/dict/words]
  --tlds-file TLDS_FILE
                        file with list of tlds [tlds.txt]
  --tlds TLDS           manually specify tlds as comma-separated list
  --leet                generate domains that replace letters with numbers
  --min-size MIN_SIZE
  --max-size MAX_SIZE
```

### Example:

Use with [dom](https://github.com/zachwill/dom/) to automatically find out if
domains are available:

```bash
for i in $(python tld.py --tlds at)
do
  dom $i
done
```
