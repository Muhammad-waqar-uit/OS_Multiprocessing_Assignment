from multiprocessing.pool import Pool

import requests

from timer import timer

URL = 'https://httpbin.org/uuid'


def fetch(web, url):
    with web.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 1)
def main():
    with Pool() as pool:
        with requests.Session() as web:
            pool.starmap(fetch, [(web, URL) for _ in range(100)])
