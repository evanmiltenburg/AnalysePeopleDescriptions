import json
import glob
from collections import Counter, defaultdict
from pprint import pprint

def load_json(filename):
    "Load a JSON file."
    with open(filename) as f:
        return json.load(f)

# Load the different categories:
filenames = glob.glob('./category_counts/*.json')
loaded = {filename: set(load_json(filename).keys()) for filename in filenames}

counts = Counter()
for values in loaded.values():
    counts.update(values)

NOUNS = {"ActivityNoun", "AgeNoun","GenderedNoun","PluralMassNoun",
         "RelationNoun","GeneralNoun","StatusOccupationNoun"}

mod_counts = Counter({k:v for k,v in counts.items() if k not in NOUNS})
noun_counts = Counter({k:v for k,v in counts.items() if k in NOUNS})

print("Modifiers &",', '.join([f'{key} ({value})' for key,value in mod_counts.most_common()]),'\\\\')
print("Nouns &",', '.join([f'{key} ({value})' for key,value in noun_counts.most_common()]),'\\\\')

mapping = {'./category_counts/Shetty-et-al-2017.json': "7",
           './category_counts/Shetty-et-al-2016.json': "4",
           './category_counts/Vinyals-et-al-2017.json': "3",
           './category_counts/Mun-et-al-2017.json': "6",
           './category_counts/Wu-et-al-2016.json': "9",
           './category_counts/Tavakoli-et-al-2017.json': "1",
           './category_counts/Dai-et-al-2017.json': "5",
           './category_counts/Liu-et-al-2017.json': "8",
           './category_counts/Zhou-et-al-2017.json': "2"}

per_modifier = defaultdict(list)
for name, cats in loaded.items():
    mods = cats - NOUNS
    for mod in mods:
        per_modifier[mod].append(mapping[name])

for name in per_modifier:
    per_modifier[name].sort()
    per_modifier[name] = ','.join(per_modifier[name])

pprint(per_modifier)
