import re
import requests
from clint.textui import progress
import logging
import os
from urllib.parse import urlparse

url = open('url.txt','r').read()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


res = requests.get(url, stream=True,headers=headers)
total_length = int(res.headers.get('content-length'))
if 'content-disposition' in res.headers:
    d = res.headers['content-disposition']
    fname = re.findall("filename=(.+)", d)[0]
else:
    a = urlparse(url)
    fname = os.path.basename(a.path)
    
fpath = f'download/{fname}'

with open(fpath, "wb") as file:
    for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1, width=100):
        if chunk:
            file.write(chunk)
print(f"file {fpath} download complete")
