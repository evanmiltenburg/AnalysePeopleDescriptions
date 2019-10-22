import spacy
import nltk
from nltk import ChartParser

# Load grammar.
grammar = nltk.data.load('./Resources/Grammar/full_grammar.cfg')
parser = ChartParser(grammar)

# Load SpaCy
nlp = spacy.load('en_core_web_sm', disable=["ner"])


def load_base_labels():
    "Load the base labels. These are not meaningful for our analysis."
    with open('./Resources/base_labels.txt') as f:
        return {line.strip() for line in f if not line == ''}

BASE_LABELS = load_base_labels()

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


def analyze_sentence(sentence, head_nouns):
    "Analyze a sentence and return all person labels with the relevant categories"
    chunks = get_chunks(sentence)
    selection = select_chunks(chunks, head_nouns)
    results = []
    for item in selection:
        result = parser.parse(item)
        labels = {subtree.label() for tree in result for subtree in tree.subtrees()}
        # Result
        person_label = ' '.join(item)
        meaningful_labels = labels - BASE_LABELS
        results.append((person_label,meaningful_labels))
    return results


gendered_nouns = load_lexicon('./Resources/Grammar/Nouns/gendered.txt')
results = analyze_sentence("There is a young black man in the garden with a tall woman.", 
                           gendered_nouns)

for label, analysis in results:
    print(label,'\t',analysis)
