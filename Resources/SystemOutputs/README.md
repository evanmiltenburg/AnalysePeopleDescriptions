# Analysing system outputs

This folder contains all code and data to analyse the system outputs.

## Folder structure

### Outputs
This folder contains the outputs themselves.

### Analyse-heads
* This folder contains a script to obtain a list of all noun heads, which outputs 
a .txt file with all nominal heads in all the captions generated by the systems.
The `heads-to-include.xlsx` file contains a manual categorisation of these heads.

### Analyse-modifiers
* The folder contains a script `build_index.py` to count all the noun chunks in the
system outputs. All counts are stored in `noun_chunk_counts.json`. 
* The script `get_relevant_chunks.py` selects all chunks that end with a phrase
that is listed in the noun inventory of our grammar. These chunks are listed in
`human_chunks.txt`
* The script `check_coverage.py` checks coverage of our grammar after only adding
the nominal heads.
* The script `keep_checking_coverage.py` checks coverage of the latest version of 
our grammar.
* The file `not-covered.txt` lists all chunks that are not covered by our grammar.

### Analyse-all
* `select_chunks.py` selects the chunks that make reference to people, and combines
those with the noun chunk counts (both source files are generated earlier).
Generates `human_chunk_counts.json`.
* `analyse_labels.py` analyses the labels using our grammar, and generates `analyses.json`.
* `system_stats.py` analyses the data on a per-system basis, and generates the `category_counts` folder, as well as `main_table.tex`
* `check_overlap.py` checks to see how many systems produce labels of a particular kind.
