#!/usr/bin/env python3

'''
Python script to download pdf slides from ithome cyber security events.
'''

import os
from pathlib import Path
import sys
from urllib.parse import unquote

from bs4 import BeautifulSoup
import requests

PREFIX_DIR = 'Download_Files'


def download_slides(page_url=None):
    '''
    Download the specified files of certions types/extentions.
    '''

    resp = requests.get(page_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if link and 'href' in link.attrs and len(link['href']) > 5 and link['href'][-4:] == '.pdf':
            slide_link = link['href']
            print('Trying to download file from link: {}'.format(slide_link))
            base_name = slide_link.split('/')[-1]
            base_name = unquote(base_name)
            file_name = '{}/{}'.format(PREFIX_DIR, base_name)
            local_path = Path(file_name)
            if local_path.is_file() and local_path.exists():
                print('{} file is already downloaded'.format(file_name))
                continue

            with requests.get(slide_link) as resp:
                with open(file_name, 'wb') as local_file:
                    local_file.write(resp.content)


if __name__ == '__main__':
    prefix_dir = Path(PREFIX_DIR)
    if not(prefix_dir.exists() and prefix_dir.is_dir()):
        os.makedirs(PREFIX_DIR)

    if len(sys.argv) > 1:
        download_slides(sys.argv[1])
