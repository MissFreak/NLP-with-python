# 参考https://blog.csdn.net/u013781175/article/details/103623905
import os
import math
import json
import requests
from copy import deepcopy


URL = 'http://www.szse.cn/api/disc/announcement/annList'

HEADER = {
    'Host': 'www.szse.cn',
    'Origin': 'http://www.szse.cn',
    'Referer': 'http://www.szse.cn/disclosure/listed/fixed/index.html',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'X-Request-Type': 'ajax',
    'X-Requested-With': 'XMLHttpRequest',
}

PAGE_SIZE = 30

PAYLOAD = {
    'channelCode': ["fixed_disc"],
    'pageNum': 1,
    'pageSize': PAGE_SIZE,
    'seDate': ["", ""],
    'stock': ["000001"],
}

PDF_URL_PREFIX = 'http://disc.static.szse.cn/download'


def get_pdf_url(code, begin_date, end_date):
    pdf_urls = []
    payload = deepcopy(PAYLOAD)
    payload['stock'] = [code]
    payload['seDate'] = [begin_date, end_date]
    res = requests.post(URL, data=json.dumps(payload), headers=HEADER).json()
    for i in res['data']:
        file_name = '_'.join([i['title'], ''.join(i['publishTime'].split()[0].split('-'))])
        pdf_url = PDF_URL_PREFIX + i['attachPath']
        pdf_urls.append((file_name, pdf_url))
    page_count = math.ceil(res['announceCount'] / PAGE_SIZE)
    for j in range(page_count - 1):
        payload['pageNum'] = j + 2
        res = requests.post(URL, data=json.dumps(payload), headers=HEADER).json()
        for i in res['data']:
            file_name = '_'.join([i['title'], ''.join(i['publishTime'].split()[0].split('-'))])
            pdf_url = PDF_URL_PREFIX + i['attachPath']
            pdf_urls.append((file_name, pdf_url))
    return pdf_urls


def save_pdf(code, path='./', begin_date='', end_date=''):
    pdf_urls = get_pdf_url(code, begin_date, end_date)
    file_path = os.path.join(path, code)
    if not os.path.isdir(file_path):
        os.makedirs(file_path)
    for file_name, url in pdf_urls:
        extension = url.split('.')[-1]
        file_full_name = os.path.join(file_path, '.'.join([file_name, extension])).replace('*', '')
        rs = requests.get(url, stream=True)
        with open(file_full_name, "wb") as fp:
            for chunk in rs.iter_content(chunk_size=10240):
                if chunk:
                    fp.write(chunk)


if __name__ == '__main__':
    # 下载全部报告
    save_pdf('000001')
    # 下载一段时间内的报告
    save_pdf('000002', begin_date='2018-12-27', end_date='2019-12-27')