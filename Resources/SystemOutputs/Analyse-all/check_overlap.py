import json
import glob
from collections import Counter

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
