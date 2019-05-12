# import requests
from requests.exceptions import RequestException
# from urllib.parse import urlencode
# import json
# from bs4 import BeautifulSoup
# import re
# from config import *
# import pymongo

import json
import os
from urllib.parse import urlencode
import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
import hashlib
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError
from config import *
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["toutiao"]
def get_page_page_index(offset,keyword):
    data = {
        'aid': '24',
        'app_name': 'web_search',
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
    }
    # data = {
    #     'aid': '24',
    #     'app_name': 'web_search',
    #     'offset':'0',
    #     'format':'json',
    #     'keyword':'街拍',
    #     'autoload': 'true',
    #     'count': '20',
    #     'en_qc': '1',
    #     'cur_tab':'1',
    #     'from':'search_tab',
    #     'pd':'synthesis',
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'cookie': 'tt_webid=6689770852458677768; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16aa738630e890-02daeed22a3bba-f353163-1fa400-16aa738630f86c; tt_webid=6689770852458677768; csrftoken=85f646aac651995d0f0d477d9e1000b1; s_v_web_id=a9c80360734866fb880cd48244e4d2e3; CNZZDATA1259612802=1806456525-1557579889-https%253A%252F%252Fwww.baidu.com%252F%7C1557585289; __tasessionId=b9cl244be1557590374034; passport_auth_status=be3918f20b2cefdeae2de53331bb068a; sso_uid_tt=9364aef949fb1422b0d8445d87b9adb1; toutiao_sso_user=08d9d869618fc319637f6e2e11d3981e; login_flag=a7eae77d77aac773723e3468446bfa02; sessionid=7bf2d480f660db06fd489845e59608a1; uid_tt=555598b2d1b7b155f07da91a6fd45192; sid_tt=7bf2d480f660db06fd489845e59608a1; sid_guard="7bf2d480f660db06fd489845e59608a1|1557590405|15552000|Thu\054 07-Nov-2019 16:00:05 GMT'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    # url = "https://www.toutiao.com/search_content/?"+urlencode(data)
    # url = "https://www.toutiao.com/search_content/?"+urlencode(data)
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get("data"):
            yield item.get('article_url')

def get_page_detail(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'cookie': 'tt_webid=6689770852458677768; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16aa738630e890-02daeed22a3bba-f353163-1fa400-16aa738630f86c; tt_webid=6689770852458677768; csrftoken=85f646aac651995d0f0d477d9e1000b1; s_v_web_id=a9c80360734866fb880cd48244e4d2e3; CNZZDATA1259612802=1806456525-1557579889-https%253A%252F%252Fwww.baidu.com%252F%7C1557585289; __tasessionId=b9cl244be1557590374034; passport_auth_status=be3918f20b2cefdeae2de53331bb068a; sso_uid_tt=9364aef949fb1422b0d8445d87b9adb1; toutiao_sso_user=08d9d869618fc319637f6e2e11d3981e; login_flag=a7eae77d77aac773723e3468446bfa02; sessionid=7bf2d480f660db06fd489845e59608a1; uid_tt=555598b2d1b7b155f07da91a6fd45192; sid_tt=7bf2d480f660db06fd489845e59608a1; sid_guard="7bf2d480f660db06fd489845e59608a1|1557590405|15552000|Thu\054 07-Nov-2019 16:00:05 GMT'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile("gallery: JSON.parse\((\".*?\")\\),.*?siblingList",re.S)
    result = re.search(images_pattern,html)
    # print(result)
    if result:
        data = json.loads(result.group(1)).replace('\\', '')
        # print(data)
        data = eval(data)
        if data and "sub_images" in data.keys():
            # print(data)
            sub_images = data.get("sub_images")
            images = [item.get('url') for item in sub_images]
            for image in images:download_image(image)
            # if images:
            #     images = images
            return {
                'title':title,
                'url':url,
                'image':images,
            }

def save_to_mongo(result):
    if db['toutiao'].insert(result):
        print('存储到MongoDB成功',result)
        return True
    return False
def download_image(url):
    print('正在下载',url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'cookie': 'tt_webid=6689770852458677768; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16aa738630e890-02daeed22a3bba-f353163-1fa400-16aa738630f86c; tt_webid=6689770852458677768; csrftoken=85f646aac651995d0f0d477d9e1000b1; s_v_web_id=a9c80360734866fb880cd48244e4d2e3; CNZZDATA1259612802=1806456525-1557579889-https%253A%252F%252Fwww.baidu.com%252F%7C1557585289; __tasessionId=b9cl244be1557590374034; passport_auth_status=be3918f20b2cefdeae2de53331bb068a; sso_uid_tt=9364aef949fb1422b0d8445d87b9adb1; toutiao_sso_user=08d9d869618fc319637f6e2e11d3981e; login_flag=a7eae77d77aac773723e3468446bfa02; sessionid=7bf2d480f660db06fd489845e59608a1; uid_tt=555598b2d1b7b155f07da91a6fd45192; sid_tt=7bf2d480f660db06fd489845e59608a1; sid_guard="7bf2d480f660db06fd489845e59608a1|1557590405|15552000|Thu\054 07-Nov-2019 16:00:05 GMT'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)
            return response.text
        return None
    except RequestException:
        print('请求图片出错')
        return None
def save_image(content):
    #创建md5对象
    m = hashlib.md5()
    #对二进制进行加密
    m.update(content)
    file_path = "%s\\%s\\%s.%s"%(os.getcwd(),"Toutiao",m.hexdigest(),'jpg')
    folder_path = '%s\\%s'%(os.getcwd(),"Toutiao")
    #判断文件夹是否存在 不存在就创建新的文件夹
    mkdir(folder_path)
    #如果文件不存在就写入到文件中
    if not os.path.exists(file_path):
        with open(file_path,"wb") as f:
            #打印
            f.write(content)
            f.close()

def mkdir(path):

    folder = os.path.exists(path)

    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print ("---  Creating  ---")
    else:
        print ("---  There is this folder!  ---")
def main(offset):
    html = get_page_page_index(offset,'街拍')
    for url in parse_page_index(html):
        if url:
            # print(url)
            html = get_page_detail(url)
            # print(html)
            if html:
                result = parse_page_detail(html,url)
                if result:
                    save_to_mongo(result)


if __name__ == '__main__':
    groups = [x*20 for x in range(1,6)]
    pool = Pool()
    pool.map(main,groups)