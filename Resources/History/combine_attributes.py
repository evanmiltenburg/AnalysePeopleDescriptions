import glob
import re

CATEGORY = re.compile('Categories/(.+).txt')

def get_category(path):
    "Extract category name from the path."
    result = CATEGORY.search(path)
    return result.group(1)


def create_index(filenames):
    "Create an index of all categories with their corresponding terms."
    index = dict()
    for filename in filenames:
        category = get_category(filename)
        with open(filename) as f:
            index[category] = [line.strip() for line in f]
    return index


def combine_indices(index1, index2):
    "Combine two indices into one."
    new_index = dict()
    shared_keys = set(index1) & set(index2)
    only1 = set(index1) - set(index2)
    only2 = set(index2) - set(index1)
    for key in shared_keys:
        values = sorted(set(index1[key] + index2[key]))
        new_index[key] = values
    for key in only1:
        new_index[key] = sorted(index1[key])
    for key in only2:
        new_index[key] = sorted(index2[key])
    return new_index


def write_to_folder(index, folder):
    "Write all category files to a folder."
    for category, entries in index.items():
        with open(folder + category + '.txt','w') as f:
            f.write('\n'.join(entries))

def update_numbers(index):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
               'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
               'sixteen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty',
               'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one-hundred']
    numbers.extend(map(str,range(100)))
    index['number'].extend(numbers)
    index['number'] = sorted(set(index['number']))


index1 = create_index(glob.glob('./Flickr30K-Categories/*.txt'))
index2 = create_index(glob.glob('./VisualGenome-Categories/*.txt'))
combined = combine_indices(index1, index2)
update_numbers(combined)
write_to_folder(combined, './Combined-Categories/')
