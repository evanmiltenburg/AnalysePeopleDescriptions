import json

def load_json(filename):
    "Load a JSON file."
    with open(filename) as f:
        return json.load(f)


def load_strings(filename):
    "Load a list of strings from a file."
    with open(filename) as f:
        return [line.strip() for line in f]

# Make a selection:
chunk_counts = load_json('../Analyse-modifiers/noun_chunk_counts.json')
human_chunks = load_strings('../Analyse-modifiers/human_chunks.txt')

human_chunk_counts = dict()
for system, counts in chunk_counts.items():
    human_chunk_counts[system] = {k:v for k,v in counts.items() 
                                      if k in human_chunks}

with open("human_chunk_counts.json", 'w') as f:
    json.dump(human_chunk_counts, f, indent=2)
