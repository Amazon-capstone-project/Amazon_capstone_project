# -*- coding: utf-8 -*-
#
# Common functions for reading / dumping data.
#

import requests
import json

from typing import List, Set, Dict, Tuple, Optional

def load_jsonl(input_path) -> List[dict]:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data

def to_jsonl(data: List[dict], dest_file: str):
    """
    Write a list of dict to a jsonl file.
    """
    with open(dest_file, 'w') as outfile:
        for entry in data:
            json.dump(entry, outfile)
            outfile.write('\n')
    print("Dumped {} records to '{}'".format(len(data), dest_file))

SAMPLE_POSTS_RAW = "data/6000_posts_sample.jsonl"

SAMPLE_COMMENTS =  "data/comments_from_sample.jsonl"

SAMPLE_POSTS_TREE = "data/sample_posts_comments.jsonl"
