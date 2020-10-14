import requests
import json
from typing import List, Set, Dict, Tuple, Optional

FILE_PATH = "data/6000_posts_sample.jsonl"

def load_jsonl(input_path) -> list:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data

def to_jsonl(target,dest_file):
    with open(dest_file, 'w') as outfile:
        for entry in target:
            json.dump(entry, outfile)
            outfile.write('\n')

def get_comment_content_by_id(c_id: str) -> str:
    """
    get the string of a comment
    """
    url = 'https://api.stackexchange.com/2.2/comments/{cid}?order=desc&sort=creation&site=stackoverflow&filter=!9_bDE0.uJ'.format(cid = c_id)
    resp = requests.get(url)
    print(url)
    try:
        items = resp.json().get('items')
        print(items)
        if len(items) > 0:
            return {
                "cid": c_id, "body": items[0].get('body_markdown')
            }
        else:
            return None
    except Exception as ex:
        print(ex)
        return None

def get_comments_by_pid(pids: List[str]) -> List[str]:
    """
    get the body markdown of comments by post ids.
    """
    pattern = "https://api.stackexchange.com/2.2/posts/{pids}/comments?pagesize=100&order=desc&sort=creation&site=stackoverflow&filter=!SYCmj)y1jqm-OsJc)7"
    pids_str = ";".join(pids)
    url = pattern.format(pids = pids_str)
    print(url)
    size = 0
    items = []
    try:
        resp = requests.get(url)
        items = resp.json().get('items')
        size = len(items)
        remainder = resp.json().get('quota_remaining')
    except Exception as ex:
        print(ex)
    else:
        print("{} comments added; remaining quota: {}.".format(size, remainder))
    finally:
        return items


def replace_comments(ids: list) -> list:
    """
    generate a list of {cid: str, body: str} from a list of ids
    """
    return [get_comment_content_by_id(c_id) for c_id in ids]

def replace_post(post: dict) -> None:
    post["comments"] = replace_comments(post["comments"])
    # print(post["answers"])
    if "answers" not in post or post["answers"] is None:
        return
    for k, v in (post["answers"]).items():
        post["answers"][k]["comments"] = replace_comments(v["comments"])

def search_pids(posts: List[dict]) -> List[str]:
    results = set()
    for p in posts:
        if "answers" in p and type(p["answers"]) is dict:
            for ans in p["answers"].values():
                results.add(str(ans.get("answer_id")))
                results.add(str(ans.get("question_id")))
    return list(results)

def batch_request(pids: List[str]) -> List[dict]:
    results = list()
    start = 0
    while start <= len(pids):
        batch = pids[start:(start + 50)]
        comments = get_comments_by_pid(batch)
        results.extend(comments)
        start += 50
    return results

if __name__ == "__main__":
    posts = load_jsonl(FILE_PATH)
    pids = search_pids(posts)
    pids = pids[1000:]
    comments = batch_request(pids)
    to_jsonl(comments, "data/shared/comments_from_sample.jsonl")
