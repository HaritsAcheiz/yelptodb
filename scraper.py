import httpx
from dataclasses import dataclass, asdict
from selectolax.parser import HTMLParser

@dataclass
class Yelper:
    base_url: str = 'https://www.yelp.com'

    def fetch_detail_url(self):
        search_endpoint = '/search?find_desc=Pet+Shop&find_loc=San+Francisco%2C+CA%2C+United+States&start=10'
        url = self.base_url + search_endpoint
        client = httpx.Client()
        response = client.get(url)
        return response.text

    def parser_detail_url(self, html):
        tree = HTMLParser(html)
        detail_urls = list()
        child = tree.css('html > body > yelp-react-root > div > div:nth-of-type(4) > div > div > div > div > main > div > ul > li')
        print(len(child))
        for item in child:
            try:
                detail_url = item.css_first('div > div > div > div:nth-of-type(2) > div > div > div > div > div > div > div > h3 > span > a').attributes['href']
                detail_urls.append(self.base_url + detail_url)
            except:
                continue
        return detail_urls

    def fetch_data(self):
        pass

    def parser_data(self):
        pass

    def main(self):
        search_html = self.fetch_detail_url()
        detail_urls = self.parser_detail_url(search_html)
        print(detail_urls)

if __name__ == '__main__':
    scraper = Yelper()
    scraper.main()