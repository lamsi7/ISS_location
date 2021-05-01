import requests
import shutil
import gzip
import os, os.path

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename

def extract_gz(filename):
    with gzip.open(filename, 'rb') as f_in:
        with open(filename.replace('.gz',''), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)    