# Reorganizing the category files

This project is based on an earlier project to manually sort the modifiers from
Flickr30K and the Visual Genome dataset. We made the following changes:

* We combined the two sets of category files into one set of category files, using `python combine_attributes.py`
* We manually revised the category files, so that they are more intuitive.
* We automatically checked for overlap between the lists, using `python analyze_overlap.py`
* We manually corrected entries that shouldn't be in multiple lists.

The result can be found in the `./Revised-categories/` folder.
