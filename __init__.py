import re
import requests
from clint.textui import progress
import logging

url = open('url.txt','r').read()

res = requests.get(url, stream=True)
total_length = int(res.headers.get('content-length'))
d = res.headers['content-disposition']
fname = re.findall("filename=(.+)", d)[0]

fpath = f'download/{fname}'

with open("fpath", "wb") as file:
    for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1, width=100):
        if chunk:
            file.write(chunk)
logging.info(f"file {fname} download complete")
