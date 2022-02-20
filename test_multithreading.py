from concurrent.futures import ThreadPoolExecutor

import requests

from timer import timer

URL = 'https://httpbin.org/uuid'


def fetch(web, url):
    with web.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 5)
def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as web:
            executor.map(fetch, [web] * 100, [URL] * 100)
            executor.shutdown(wait=True)
