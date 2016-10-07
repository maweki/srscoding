# srs coding calc

calculate the smallest coding compatible with the rewriting relationship described by Geser, Waldmann, Wenzel
at WST 2016 (http://cl-informatik.uibk.ac.at/events/wst-2016/) using the theorem `forall a,b in C^+: forall o in OVL(a,b): o in C^+`.


Usage: `python3 coding.py w1 w2 w3 ...`

Example:

```
$ python3 coding.py bca aabc
frozenset({'bc', 'a'})
```
