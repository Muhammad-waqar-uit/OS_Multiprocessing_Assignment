import requests

from timer import timer

URL = 'https://httpbin.org/uuid'


def fetch(web, url):
    with web.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 1)
def main():
    with requests.Session() as web:
        for i in range(100):
            fetch(web, URL)
