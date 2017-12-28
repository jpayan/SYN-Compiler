import globals
from re import split
from lexical_analyzer import analyze_lexis
from syntactic_analyzer import analyze_syntax
from semantic_analyzer import analyze_semantic


def read_input(source_code):
    return [word for line in open(source_code, 'r') for word in
            split(r'(\.+|"\s+"|\s+|\(+|\[+|:+|\)|\]+|;+|<-+|\++|-+|\*+|/+|>=+|<=+|>+|<+|==+|\|\|+|&&+|!=+)', line)]


def write_output(name, content):
    output = open(name, 'w')
    for item in content:
        output.write('%s\n' % str(item))
    output.close()


def write_results():
    write_output('tokens.txt', globals.tokens)
    write_output('symbols.txt', globals.symbols)
    write_output('errors.txt', globals.errors)
    write_output('grammar_rules.txt', globals.grammar_rules)
    # write_output('quadruplets.txt', globals.quadruplets)


def main():
    globals.init()

    globals.source_code = read_input("syn_code.txt")

    # ----------------------------------- Lexical Analyzer -----------------------------------#
    analyze_lexis()

    # ---------------------------------- Syntactic Analyzer ----------------------------------#
    analyze_syntax()

    # ---------------------------------- Semantic Analyzer  ----------------------------------#
    analyze_semantic()

    write_results()


if __name__ == '__main__':
    main()
