import json
import nltk
from nltk import ChartParser


def load_json(filename):
    "Load a JSON file."
    with open(filename) as f:
        return json.load(f)


def load_strings(filename):
    "Load a list of strings from a file."
    with open(filename) as f:
        return [line.strip() for line in f]

def analyse(human_chunks, parser, labels_to_ignore):
    "Analyse a list of human chunks and return a dictionary with the results."
    analysis = dict()
    for chunk in human_chunks:
        chunk_as_list = chunk.split()
        try:
            result = parser.parse(chunk_as_list)
            labels = {subtree.label() for tree in result for subtree in tree.subtrees()}
            meaningful_labels = labels - labels_to_ignore
            analysis[chunk] = list(meaningful_labels)
        except ValueError:
            print(f"Could not analyse chunk: {chunk}")
            analysis[chunk] = None
    return analysis


# Load grammar.
grammar = nltk.data.load('../../Grammar/full_grammar.cfg')
parser = ChartParser(grammar)

IGNORE = {'S','Label','NounPhrase','Conj','Det',
          'HeadNoun','Mod','Contrast','Consist'}

human_chunks = load_strings('../Analyse-modifiers/human_chunks.txt')
analysis = analyse(human_chunks, parser, IGNORE)

with open('analyses.json','w') as f:
    json.dump(analysis, f, indent=2)
