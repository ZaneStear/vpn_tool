import json
import cloudscraper
from pathlib import Path


def check_in():
    har = json.loads(Path('mxwljsq.top.har').read_text())
    r_body = har['log']['entries'][0]['request']
    method = r_body['method']
    url = r_body['url']
    headers = r_body['headers']
    cookies = r_body['cookies']
    head = {}
    for header in headers:
        if str(header['name']).startswith(':'):
            header['name'] = str(header['name']).lstrip(':')
        head[header['name']] = header['value']
    result = cloudscraper.create_scraper().post(url, headers=head)
    print("签到结束: "+result.text)


if __name__ == '__main__':
    check_in()
    pass