# Outdated posts recoginition pipeline

## Extract potentially outdated posts

`extract_outdated.py`

- Load files about comments & answers that are tagged with AWS.

## Extract heuristic features

### Linguistic

- Using [`spaCy`](https://spacy.io/usage/linguistic-features), we sentencify the text and identify th subjectives.
- Phrase 'out of date' is replaced by 'outdated' during the analysis.
