# Example analysis

This folder shows how to analyze your own system outputs. 

## Usage
Run `python example.py`. Requirements are the same as the main repository.

The code takes the outputs from the `caption_outputs` folder as an input.
Your own outputs don't need to share this format, but then you need to modify the output-specific code (i.e. the code below `if __name__ == "__main__"`). 

The code produces the analyses in the `analyses` folder. There are two files per system:
1. `base_name-index.json` lists the labels referring to people, with a list of IDs of captions these labels occur in.
2. `base_name-analysis.json` provides an analysis of the individual labels.

Together, these files provide a summary of the person-labels used in your caption data.
The code is minimally optimized for speed (e.g. by analyzing types rather than tokens).
If you need a more efficient implementation, there are probably some tricks you can still use.

## Data
I have used system outputs from [Annika Lindh's GitHub](https://github.com/AnnikaLindh/Controllable_Region_Pointer_Advancement) as an example. These examples are released under the BSD 2 license. If you use this data, please be kind to Annika and cite her:

```
@inproceedings{lindh_language-driven_2020,
	address = {Barcelona, Spain (Online)},
	title = {Language-{Driven} {Region} {Pointer} {Advancement} for {Controllable} {Image} {Captioning}},
	url = {https://www.aclweb.org/anthology/2020.coling-main.174},
	booktitle = {Proceedings of the 28th {International} {Conference} on {Computational} {Linguistics}},
	publisher = {International Committee on Computational Linguistics},
	author = {Lindh, Annika and Ross, Robert J. and Kelleher, John D.},
	month = dec,
	year = {2020},
	pages = {1922--1935}
}
```
