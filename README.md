# SemanticAttributes
CFG to identify semantic attributes (in automatic image descriptions)

## Requirements
These are the software versions that we used. Other versions remain untested, and may give different results.

* Python 3.6.6
* NLTK 3.3
* SpaCy 2.0.4

## Contents

* `example.py` shows the basic usage of this resource.
* `Resources` contains the grammar, the lexicon, and the scripts used to build the grammar.
    - `History` contains the previous versions of the lexicon, with the scripts that we used to compile the current version.
    - `Nouns` contains the set of nouns used in our grammar. The grammar does not provide full coverage of all nouns, but rather aims to provide an accurate analysis for the nouns that are given.
    - `Other` contains other terms that are essential for the grammar to work.

## Usage

Run `python example.py` to see an analysis of the sentence "There is a young man in the garden with a tall woman."
