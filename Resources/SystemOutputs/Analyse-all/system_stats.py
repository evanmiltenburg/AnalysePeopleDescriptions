import json
import re
from collections import Counter
from tabulate import tabulate

def load_json(filename):
    "Load a JSON file."
    with open(filename) as f:
        return json.load(f)


def dump_json(data, filename):
    "Write a JSON file."
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def simplify_keys(d):
    "Simplify the keys."
    return {k.split('/')[2]:v for k,v in d.items()}


def category_counter(counts):
    "Get counts for all categories."
    c = Counter()
    for label, frequency in counts.items():
        analysis = analyses[label]
        if analysis is not None:
            c.update(analysis * frequency)
    return c


def total_modifiers(category_counts):
    "Total number of modifiers."
    return sum(count for category, count in category_counts.items() 
                     if not category in NOUNS)


def num_category_types(category_counts):
    "Number of category types."
    types = set(category_counts.keys())
    modifiers = types - NOUNS
    nouns = types - modifiers
    return len(modifiers), len(nouns)


def create_table(data):
    "Create table for the paper."
    rows = []
    for system, counts in data.items():
        num_labels = sum(counts.values())
        category_counts = category_counter(counts)
        dump_json(category_counts,f'./category_counts/{system}.json')
        num_modifiers = total_modifiers(category_counts)
        avg_modifiers = (num_modifiers/num_labels)
        num_mod_types, num_noun_types = num_category_types(category_counts)
        row = [system, num_labels, num_modifiers, f'{avg_modifiers:.2f}', num_mod_types, num_noun_types]
        rows.append(row)
    return tabulate(rows, headers=['System', '#Labels', '#Mods', 'Avg-mods', 'Mod-types', 'Noun-types'], tablefmt='latex_booktabs')


NOUNS = {"ActivityNoun", "AgeNoun","GenderedNoun","PluralMassNoun",
         "RelationNoun","GeneralNoun","StatusOccupationNoun"}
analyses           = load_json("analyses.json")
human_chunk_counts = load_json("human_chunk_counts.json")
human_chunk_counts = simplify_keys(human_chunk_counts)
table = create_table(human_chunk_counts)
with open('main_table.tex','w') as f:
    f.write(table)
