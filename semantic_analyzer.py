import re
import globals


def filer_rules(grammar_rules):
    rules = []
    for item in grammar_rules:
        if re.match(r'[DAL]', item[0]):
            rules.append(item)
    return rules


def analyze(grammar_rules):
    for item in grammar_rules:
        rule = item[0]
        tokens_fragment = re.compile(r'' + item[1])

        tuples = []

        for instance in tokens_fragment.finditer(''.join(globals.tokens)):
            tuples.append(globals.symbols[instance.start(): instance.end()])

        if tuples:
            if rule == 'D':
                print(str(tuples))
            if rule == 'A':
                print(str(tuples))
            if rule == 'L':
                print(str(tuples))


def analyze_semantic():
    print(globals.grammar_rules)
    rules = filer_rules(globals.grammar_rules)
    analyze(rules)
