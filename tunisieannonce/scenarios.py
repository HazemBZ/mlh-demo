from helpers.agents import FFAgent
from helpers.parsers import AnnouncementParser


class AnnnouncementScenario:
    target = "http://www.tunisie-annonce.com"
    signin = "http://www.tunisie-annonce.com/LoginUser.asp"

    def __init__(self):
        parser = AnnouncementParser

        self.login = parser.get_login("tunisie_annonce")
        self.password = parser.get_password("tunisie_annonce")

    def run(self):
        a = FFAgent(self.target)
        print("agent started")
        self.agent = a
