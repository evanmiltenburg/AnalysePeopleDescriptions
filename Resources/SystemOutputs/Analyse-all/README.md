# Analysing system output

* `select_chunks.py` selects the chunks that make reference to people. Generates `human_chunk_counts.json`.
* `analyse_labels.py` analyses the labels using our grammar, and generates `analyses.json`.
* `system_stats.py` analyses the data on a per-system basis, and generates the `category_counts` folder, as well as `main_table.tex`
* `check_overlap.py` checks to see how many systems produce labels of a particular kind.
