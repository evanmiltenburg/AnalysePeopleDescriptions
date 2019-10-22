from itertools import combinations
import glob
import csv


def get_filename(path):
    "Quick way to get the filename."
    return path.split('/')[-1][:-4]


def get_lines(filename):
    "Get lines from a file."
    with open(filename) as f:
        return [line.strip() for line in f]


def build_index(path_pattern):
    "Build index of unique lines per file."
    index = dict()
    category_files = glob.glob(path_pattern)
    for path in category_files:
        lines = get_lines(path)
        filename = get_filename(path)
        index[filename] = set(lines)
    return index


def compute_overlap(index):
    overlap = dict()
    for a,b in combinations(index.keys(),2):
        overlap[(a,b)] = index[a] & index[b]
    return overlap


def overlap_to_rows(overlap_index):
    "Generate rows from the overlap index."
    rows = [['file1', 'file2', 'overlap']]
    for files, overlap in overlap_index.items():
        if overlap:
            file1, file2 = files
            overlap = ', '.join(overlap)
            row = [file1, file2, overlap]
            rows.append(row)
    return rows


if __name__ == '__main__':
    index = build_index('./Combined-Categories/*.txt')
    overlap = compute_overlap(index)
    rows = overlap_to_rows(overlap)
    with open('overlap.tsv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(rows)
