import spacy
import nltk
from nltk import ChartParser

# Load grammar.
grammar = nltk.data.load('./Resources/full_grammar.cfg')
parser = ChartParser(grammar)

# Load SpaCy
nlp = spacy.load('en_core_web_sm')


def load_base_labels():
    "Load the base labels. These are not meaningful for our analysis."
    with open('./Resources/base_labels.txt') as f:
        return {line.strip() for line in f if not line == ''}


def load_lexicon(filename):
    "Load a list of words from a file."
    with open(filename) as f:
        return [line.strip() for line in f]


def string_tokens(span):
    "Represent a span as a list of string tokens."
    return [token.orth_ for token in span]


def get_chunks(description):
    "Get noun chunks from a given description."
    doc = nlp(description)
    chunks = [string_tokens(chunk) for chunk in doc.noun_chunks]
    return chunks


def select_chunks(chunks, nouns):
    "Select chunks that end with one of the selected nouns."
    return [chunk for chunk in chunks if chunk[-1] in nouns]


base_labels = load_base_labels()
gendered_nouns = load_lexicon('./Resources/Nouns/gendered.txt')
chunks = get_chunks("There is a young black man in the garden with a tall woman.")
selection = select_chunks(chunks, gendered_nouns)

for item in selection:
    print(' '.join(item))
    result = parser.parse(item)
    labels = {subtree.label() for tree in result for subtree in tree.subtrees()}
    meaningful_labels = labels - base_labels
    print(meaningful_labels)
