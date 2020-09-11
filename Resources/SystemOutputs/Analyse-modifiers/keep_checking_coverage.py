import nltk
from nltk import ChartParser

# Load grammar.
grammar = nltk.data.load('../../Grammar/full_grammar.cfg')
parser = ChartParser(grammar)

with open('human_chunks.txt') as f:
    noun_chunks = [line.strip().split() for line in f]

not_covered = []
for chunk in noun_chunks:
    try:
        result = parser.parse(chunk)
        print(f"Valid: {chunk}")
    except ValueError:
        print(f"Not covered: {chunk}")
        chunk = ' '.join(chunk) + '\n'
        not_covered.append(chunk)

with open("not-covered.txt",'w') as f:
    f.writelines(not_covered)

num_chunks = len(noun_chunks)
num_covered = len(noun_chunks) - len(not_covered)
num_not_covered = len(not_covered)
print(f"Number of unique noun chunks: {num_chunks}")
print(f"Covered: {num_covered} ({(num_covered/num_chunks) * 100}%)")
print(f"Not covered: {num_not_covered} ({(num_not_covered/num_chunks) * 100}%)")
