# Grammar

This folder contains the CFG that is used to parse image description labels.
It is automatically generated from a manually curated lexicon.

## Files and folders

**Files**

* `base_grammar.cfg` contains the base grammar, with all the main rules. This file only contains nonterminals. The lexicon is added on later.
* `full_grammar.cfg` contains the complete grammar. Use this file for all parsing.
* `update_grammar.py` generates the complete grammar, using the settings from config.json.
* `config.json` specifies all the files from the lexicon to be used in generating the grammar.

**Folders**

* `History` contains the older lexicons, and shows how we established the current version. (See the README file inside.)
* `Nouns` contains all the nouns that we're using in our grammar.
* `Other` contains other relevant words from our lexicon.
