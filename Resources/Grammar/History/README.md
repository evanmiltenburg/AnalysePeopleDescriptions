# Reorganizing the category files

This project is based on an earlier project to manually sort the modifiers from
Flickr30K and the Visual Genome dataset. We made the following changes:

## Step 1: combining the existing data
We combined the two sets of category files into one set of category files, using `python combine_attributes.py`. The result of this can be found in the 
`./Combined-categories` folder.

## Step 2: revising the category files
* We manually revised the category files, so that they are more intuitive.
* We automatically checked for overlap between the lists, using `python analyze_overlap.py`
* We manually corrected entries that shouldn't be in multiple lists.
* We manually cleaned entries (e.g. remove characters that should not be inside terminal expressions).

The result can be found in the `./Revised-categories/` folder.

## Step 3: incorporating modifiers from system output
We analysed system output for nine different systems, to determine which modifiers
are used with the nominal heads identified in a separate stage. These modifiers
were added to the category files.

The result can be found in the `./Updated-categories` folder.
