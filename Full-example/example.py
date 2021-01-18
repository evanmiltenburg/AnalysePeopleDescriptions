import json
import glob
from collections import defaultdict
import spacy
import nltk
from nltk import ChartParser


def load_json(filename):
    "Load a JSON file."
    with open(filename) as f:
        return json.load(f)


def save_json(obj, filename):
    "Save a JSON file."
    with open(filename,'w') as f:
        json.dump(obj, f, indent=4)


def load_lexicon(filename):
    "Load a list of words from a file."
    with open(filename) as f:
        return [line.strip() for line in f]


def load_base_labels():
    "Load the base labels. These are not meaningful for our analysis."
    with open('../Resources/Grammar/base_labels.txt') as f:
        return {line.strip() for line in f if not line == ''}


def load_heads():
    "Load the heads from the grammar folder."
    noun_files = glob.glob('../Resources/Grammar/Nouns/*.txt')
    heads = {head for file_path in noun_files 
                  for head in load_lexicon(file_path)}
    head_dict = defaultdict(list)
    for head in heads:
        final_letter = head[-1]
        head_dict[final_letter].append(head)
    return head_dict


def refers_to_human(chunk, head_dict):
    "Determine whether a chunk should be included."
    final_letter = chunk[-1]
    chunk_list = chunk.split()
    for head in head_dict[final_letter]:
        head_list = head.split()
        head_len = len(head_list)
        if chunk_list[-head_len:] == head_list:
            return True
    return False


def get_human_chunks(caption, head_dict):
    "Returns a list of chunks that refer to people."
    doc = nlp(caption)
    chunks = [chunk.orth_.lower() for chunk in doc.noun_chunks]
    human_chunks = [chunk for chunk in chunks 
                          if refers_to_human(chunk, head_dict)]
    return human_chunks


def create_chunk_index(ids_captions):
    "Create index of chunks that refer to people, with ids as values."
    chunk_index = defaultdict(list)
    for identifier, caption in ids_captions:
        human_chunks = get_human_chunks(caption, head_dict)
        for chunk in human_chunks:
            chunk_index[chunk].append(identifier)
    return chunk_index


def analyze_chunk(tokens, parser):
    "Analyze a chunk and return all person labels with the relevant categories"
    result = parser.parse(tokens)
    labels = {subtree.label() for tree in result for subtree in tree.subtrees()}
    meaningful_labels = list(labels - BASE_LABELS)
    return meaningful_labels


def analyze_chunks(chunks, parser, grammar):
    "Analyze a sequence of chunks."
    analyses = dict()
    for chunk in chunk_index:
        tokens = nltk.word_tokenize(chunk)
        not_covered = missing(tokens, grammar)
        if not_covered:
            analyses.get('not_covered',[]).extend(not_covered)
            analyses.get('failed_chunks',[]).append(chunk)
        else:
            analyses[chunk] = analyze_chunk(tokens, parser)
    return analyses


def missing(tokens, grammar): 
    "Returns tokens not covered by the grammar."
    return [tok for tok in tokens 
                if not grammar._lexical_index.get(tok)]


# Load grammar.
grammar = nltk.data.load('../Resources/Grammar/full_grammar.cfg')
parser = ChartParser(grammar)
BASE_LABELS = load_base_labels()

# Load SpaCy
nlp = spacy.load('en_core_web_sm', disable=["ner"])

# Load heads defined by the grammar
head_dict = load_heads()

if __name__ == "__main__":
    # Specific code: analyze examples.
    for outputs in glob.glob('caption_outputs/*.json'):
        print(outputs)
        base_name = outputs.split('/')[-1][:-5]
        data = load_json(outputs)
        ids_captions = [(ident, caption[0]) for ident, caption in data['generated_captions'].items()]

        # Create chunk index for efficiency
        chunk_index = create_chunk_index(ids_captions)

        # Analyze all chunks
        analysis = analyze_chunks(chunk_index, parser, grammar)
        
        # Save data
        save_json(chunk_index, f'analyses/{base_name}-index.json')
        save_json(analysis, f'analyses/{base_name}-analysis.json')
