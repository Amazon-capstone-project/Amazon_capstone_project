# 10/14/2020
# author: Jiaqi Tang

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from collections import defaultdict
import json

def main():
    url='https://docs.aws.amazon.com/'
    html=request_aws(url)
    soup=BeautifulSoup(html,'lxml')
    save_to_json(soup)

def request_aws(url):
    '''
    get html source page

    :param url: aws service web url
    :return: source pare
    '''
    time.sleep(2)
    driver=webdriver.Chrome()
    driver.get(url)
    return driver.page_source

def save_to_json(soup):
    '''
    find the service dict from html source page and save as json file

    :param soup: html source page
    :return: save the dict to json
    '''
    service_dict=defaultdict(list)
    for bigli in soup.find(class_='awsui-cards-container').find_all(class_='awsui-cards-card-container'):
        head=bigli.find('h4').text.strip()
        prefix=bigli.find_all(class_='awsdocs-service-prefix ng-binding')
        suffix=bigli.find_all(class_='awsdocs-service-name ng-binding')
        for pre,suf in zip(prefix,suffix):
            service_dict[head].append(pre.text.strip()+'-'+suf.text.strip())

    with open('../data/aws_service_dict.json', 'w') as handle:
        json.dump(service_dict, handle)


if __name__ == '__main__':
    main()
