from helpers.agents import FFAgent
from helpers.parsers import AnnouncementParser
from cavatn.scraper import CavatnScraper


class AnnnouncementScenario:
    target = "https://www.cava.tn/"

    def __init__(self):
        self.login = AnnouncementParser.get_login("cava")
        self.password = AnnouncementParser.get_password("cava")

    def run(self):
        a = FFAgent(self.target)
        s = CavatnScraper()

        a.get_by_x('//a[@data-target="#login-modal"]').click()

        a.get_by_id("LoginForm_username").send_keys(self.login)
        a.get_by_id("LoginForm_password").send_keys(self.password)
        a.get_by_id("submit-btn").click()

        a.nav("https://www.cava.tn/products/create")

        s.set_cookies(a.agent.get_cookies())

        annoncement_url = s.create_announcement()

        a.terminate()
        return annoncement_url
