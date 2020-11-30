#!/usr/bin/env python
# coding: utf-8

# In[134]:


import json

import pandas as pd

#%%

PATH_COMMENTS = r'E:\Downloaded\Datasets\stackoverflow_amazon_a_comment.csv'


def load_comments_from_csv(path: str):
    _data = pd.read_csv(path, delimiter='\t')
    return _data

#%%
data = load_comments_from_csv(PATH_COMMENTS)

# In[2]:


def load_jsonl(input_path) -> list:
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data


# In[3]:


# load jsonl file to list of dictionaries
data_path = './week2/se_cs_ds.jsonl'
data = load_jsonl(data_path)


# In[167]:


# function to check for keywords in comments
def find_outdated_in_comments(data):
    outdated_comments = pd.DataFrame(columns=['Id', 'Text', 'PostId'])
    id_column = []
    text_column = []
    postid_column = []
    for post in data:
        if post['CommentCount'] != 0:
            for comment in post['comments']:
                if ('outdated' in comment['Text'] or 'deprecated' in comment['Text']
                        or 'obsolete' in comment['Text'] or 'out of date' in comment['Text']):
                    id_column.append(comment['Id'])
                    text_column.append(comment['Text'])
                    postid_column.append(comment['PostId'])
                    # print('CommentId: ', comment['Id'])
                    # print('Text: ', comment['Text'])
                    # print('PostId: ', comment['PostId'])
    outdated_comments['Id'] = id_column
    outdated_comments['Text'] = text_column
    outdated_comments['PostId'] = postid_column
    return outdated_comments


# In[168]:


# function to check for keywords in answers
def find_outdated_in_answers(data):
    outdated_answers = pd.DataFrame(columns=['Id', 'Body', 'PostId'])
    id_column = []
    body_column = []
    postid_column = []
    for post in data:
        if post['AnswerCount'] != 0:
            answers = post['answers']
            answerKeys = list(answers.keys())
            for i in range(len(answerKeys)):
                answer = answers[answerKeys[i]]
                body = answer['Body']
                if ('outdated' in body or 'deprecated' in body or 'obsolete' in body or 'out of date' in body):
                    id_column.append(answer['Id'])
                    body_column.append(answer['Body'])
                    postid_column.append(answer['ParentId'])
                    # print('AnswerId: ', answer['Id'])
                    # print('Body: ', answer['Body'])
                    # print('PostId: ', answer['ParentId'])
    outdated_answers['Id'] = id_column
    outdated_answers['Body'] = body_column
    outdated_answers['PostId'] = postid_column
    return outdated_answers


# In[169]:


outdated_comments = find_outdated_in_comments(data)

# In[172]:


outdated_answers = find_outdated_in_answers(data)

# In[ ]:
