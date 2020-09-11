import spacy
import json
import glob
from collections import Counter

nlp = spacy.load('en_core_web_sm', disable=["ner"])


def get_captions(filename):
    "Load captions from a results file."
    with open(filename) as f:
        data = json.load(f)
    return [entry['caption'] for entry in data]


def get_noun_chunk_counts(captions):
    "Get a counter with all noun chunks in the caption data."
    chunk_counts = Counter()
    for i,caption in enumerate(captions):
        print(f"Caption number {i}")
        doc = nlp(caption)
        noun_chunk_strings = [chunk.orth_.lower() for chunk in doc.noun_chunks]
        chunk_counts.update(noun_chunk_strings)
    return chunk_counts


def count_all_systems(file_pattern):
    "Count noun chunks for all systems"
    json_files = glob.glob(file_pattern)
    count_per_system = dict()
    for i,filename in enumerate(json_files, start=1):
        print("File ",i, filename)
        captions = get_captions(filename)
        count_per_system[filename] = get_noun_chunk_counts(captions)
    return count_per_system


count_per_system = count_all_systems('../Outputs/*/*.json')
with open('noun_chunk_counts.json','w') as f:
    json.dump(count_per_system, f, indent=2)

    
