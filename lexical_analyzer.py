import re
import globals


def set_mdd():
    return {
        re.compile(r'^nothing$'): 'h',
        re.compile(r'^prime$'): 'r',
        re.compile(r'^when$'): 'w',
        re.compile(r'^otherwise$'): 'o',
        re.compile(r'^or\swhen$'): 'x',
        re.compile(r'^loop$'): 'l',
        re.compile(r'^until$'): 'u',
        re.compile(r'^(num|rational|text|bool)$'): 't',
        re.compile(r'(^print$|^to_string$)'): 'f',
        re.compile(r'[()]'): 'p',
        re.compile(r'[:(;]'): 'v',
        re.compile(r'[\[\]]'): 'c',
        re.compile(r'<-|\+|-|\*|/'): 'a',
        re.compile(r'>=|<=|>|<|==|\|\||&&|!='): 'g',
        re.compile(r'^[a-zA-Z]+[a-zA-Z0-9]*$'): 'i',
        re.compile(r'^nothing$'): 'h',
        re.compile(r'^\s\s$'): 'e',
        re.compile(r'^(True|False|[-]?[0-9]+|[-]?[0-9]+\.[0-9]+|\"[^\"]*\")$'): 'm'
    }


def run_automata(mdd, source_code):
    for index, current_word in enumerate(source_code):
        match = False
        if re.match(r'(^\s$|^$|\t)', current_word):
            continue
        for key, value in mdd.items():
            if key.match(current_word):
                match = True
                globals.tokens.append(value)
                globals.symbols.append((value, current_word))
                break
        if not match:
            globals.errors.append('Error at char: "%s" at Index: %d\n' % (str(current_word), index))


def analyze_lexis():
    mdd = set_mdd()
    run_automata(mdd, globals.source_code)
