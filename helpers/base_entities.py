from requests import Session
from requests.cookies import RequestsCookieJar


class BaseScraper:
    def __init__(self, **kwargs):
        self.session = Session()
        self.session.proxies = kwargs.get('proxies')
        self.session.verify = False
        self.image_uploads = []
    
    def set_cookies(self, cookies):
        jar = RequestsCookieJar()
        for c in cookies:
            jar.set(c['name'], c['value'], domain=c['domain'], path=c['path'])
        self.session.cookies = jar
