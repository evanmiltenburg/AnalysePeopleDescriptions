import spacy
import json
import glob

nlp = spacy.load('en_core_web_sm', disable=["ner"])

def get_captions(filename):
    "Load captions from a results file."
    with open(filename) as f:
        data = json.load(f)
    return [entry['caption'] for entry in data]


def get_head(chunk):
    "Get the head of the noun chunk."
    tokens = [tok for tok in chunk]
    nouns = []
    for tok in reversed(tokens):
        if tok.pos_ == 'NOUN':
            nouns.append(tok.text)
        else:
            break
    return ' '.join(reversed(nouns))


def get_heads_from_captions(captions):
    "Get a set of all unique heads in all the captions."
    heads = set()
    for caption in captions:
        doc = nlp(caption)
        for chunk in doc.noun_chunks:
            head = get_head(chunk)
            heads.add(head)
    return heads

json_files = glob.glob('../Outputs/*/*.json')
all_heads = set()
for i,filename in enumerate(json_files, start=1):
    print("File ",i, filename)
    captions = get_captions(filename)
    unique = set(captions)
    heads = get_heads_from_captions(unique)
    all_heads.update(heads)

all_heads = sorted(all_heads)
with open('heads.txt','w') as f:
    f.write('\n'.join(all_heads))
