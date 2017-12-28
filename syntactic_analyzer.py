import re
import globals

mdd = {}
tmp = ''


def get_main_regex():
    return r'^(?P<S>hrppv(?P<E>.*)v\s?)$'


def get_declaration_regex():
    return r'^(?P<D>\s?ti(a[im](a[im])*(e)?)?(e)?)'


def get_assignation_regex():
    return r'^(?P<A>\s?ia[im](a[im])*(e)?)'


def get_conditional_regex():
    return r'^(?P<C>\s?[wx]p' + get_logical_regex()[1:] + r'pv(?P<E>.*)v\s?[xoe]?)'


def get_otherwise_regex():
    return r'^(\s?ov(?P<E>.*)v)'


def get_loop_regex():
    return r'^(?P<O>\s?lp' + get_declaration_regex()[1:] + get_logical_regex()[1:] + get_assignation_regex()[1:] + \
           r'pv(?P<E>.*)v)'


def get_until_regex():
    return r'^(?P<U>\s?up' + get_logical_regex()[1:] + r'pv(?P<E>.*)v)'


def get_logical_regex():
    return r'^(?P<L>\s?[im]g[im](a[im])*(e)?)'


def get_method_regex():
    return r'^(?P<M>\s?fp(?P<E>.*)p(e)?)'


def set_mdd():
    global mdd
    mdd = {
        re.compile(get_main_regex()): 'S',
        re.compile(get_declaration_regex()): 'D',
        re.compile(get_assignation_regex()): 'A',
        re.compile(get_conditional_regex()): 'C',
        re.compile(get_loop_regex()): 'O',
        re.compile(get_otherwise_regex()): 'T',
        re.compile(get_until_regex()): 'U',
        re.compile(get_logical_regex()): 'L',
        re.compile(get_method_regex()): 'M'
    }


def append_to_grammar_rules(group_dict):
    for item in group_dict.items():
        globals.grammar_rules.append(item)


def get_matching_group(groups):
    if 'E' in groups:
        return groups['E']
    else:
        key, value = groups.popitem()
        return value


def run_automata(tokens):
    global tmp
    if tokens:
        match = False
        for key, value in mdd.items():
            if key.match(tokens):
                match = True
                group_dict = key.match(tokens).groupdict()
                append_to_grammar_rules(group_dict)
                extract = get_matching_group(group_dict)
                if re.match(r'[DAL]', value):
                    tokens = tokens.replace(extract, '', 1)
                    run_automata(tokens)
                    break
                else:
                    tmp = extract
                    run_automata(extract)
                    break
        if not match:
            print('Did not match any grammar rules: ', tokens)


def analyze_syntax():
    set_mdd()
    run_automata(''.join(globals.tokens))
