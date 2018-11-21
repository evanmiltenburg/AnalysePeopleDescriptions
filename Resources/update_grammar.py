import json

def string_to_lexical_item(string):
    "Convert a string to a lexical item."
    tokens = string.strip().split()
    quoted_tokens = ["'{}'".format(token) for token in tokens]
    spaced_tokens = ' '.join(quoted_tokens)
    return spaced_tokens


def load_lexical_items(filename):
    "Load lexical items from a file."
    with open(filename) as f:
        return [string_to_lexical_item(line) for line in f]


def create_nonterminal_rule(label, targets, add_newline=True):
    "Create a nonterminal rule."
    components = [label, '->', ' '.join(targets)]
    rule = ' '.join(components)
    if add_newline:
        rule = rule + '\n'
    return rule


def create_lexical_rule(category_name, lexical_items, add_newline=True):
    "Generate rule."
    rule = category_name + ' -> ' + ' | '.join(lexical_items)
    if add_newline:
        rule = rule + '\n'
    return rule


def lexical_rule_from_file(category_name, filename, add_newline=True):
    "Generate rule on the basis of a vocabulary file."
    lexical_items = load_lexical_items(filename)
    rule = create_lexical_rule(category_name, lexical_items)
    return rule


def main(grammar_file, configuration):
    "Run all the code to update the grammar."
    # Load base grammar.
    with open('./base_grammar.cfg') as f:
        rules = f.readlines()
    
    # Load file index, with mapping from categories to files.
    with open(configuration) as f:
        file_index = json.load(f)
    
    # Add new rules.
    for category, filename in file_index.items():
        rule = lexical_rule_from_file(category, filename)
        rules.append(rule)
    
    # Write rules to file.
    with open(grammar_file, 'w') as f:
        f.writelines(rules)


if __name__=='__main__':
    main('full_grammar.cfg', 'config.json')
