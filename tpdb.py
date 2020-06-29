
from coding import coding


def interpret(srsfile):
    import xml.etree.ElementTree as ET
    tree = ET.parse(srsfile)
    el_problem = tree.getroot()
    el_trs = el_problem.find("trs")
    el_rules = el_trs.find("rules")
    rules = el_rules.findall("rule")
    words = set()
    for rule in rules:
        lhs = rule.find("lhs")
        fun = lhs.find("funapp")
        l = ()
        while fun is not None:
            l += (fun.findtext("name"),) if fun.findtext("name") else ()
            fun = fun.find("arg").find("funapp")
        rhs = rule.find("rhs")
        fun = rhs.find("funapp")
        r = ()
        while fun is not None:
            r += (fun.findtext("name"),) if fun.findtext("name") else ()
            fun = fun.find("arg").find("funapp")
        words.add(l)
        words.add(r)
    return words

def main():
    import sys
    f = sys.argv[1]
    sys.setrecursionlimit(100000)
    try:
        words = interpret(f)
        original_code = set().union(*words)
        if all(all(len(l) == 1 for l in w) for w in words):
            words = set(''.join(w) for w in words)
        code = coding(words)
        if any(len(c) > 1 for c in code):
            print("="*5, f, "="*5,)
            print("ORIGINAL CODING:", original_code)
            print("SMALLER CODING", code)
            print("ORIGINAL RULE SIDES:", words)
            print()
    except RecursionError:
        print("RECURSION ERROR", words, f)
        pass


if __name__ == '__main__':
    main()
