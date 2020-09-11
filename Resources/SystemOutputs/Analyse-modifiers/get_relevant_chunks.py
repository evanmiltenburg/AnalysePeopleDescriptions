import json
import glob
from collections import defaultdict


def get_chunk_types(data):
    "Get chunk types from the count data."
    chunk_types = set()
    for counts in data.values():
        chunk_types.update(counts.keys())
    return chunk_types


def load_lexicon(filename):
    "Load a list of words from a file."
    with open(filename) as f:
        return [line.strip() for line in f]


def load_heads():
    "Load the heads from the grammar folder."
    noun_files = glob.glob('../../Grammar/Nouns/*.txt')
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


with open('noun_chunk_counts.json') as f:
    data = json.load(f)

chunk_types = get_chunk_types(data)
head_dict = load_heads()
human_chunks = [chunk + '\n' for chunk in chunk_types 
                      if refers_to_human(chunk, head_dict)]
human_chunks.sort()

with open('human_chunks.txt','w') as f:
    f.writelines(human_chunks)
