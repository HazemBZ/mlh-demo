from helpers.agents import FFAgent
from helpers.parsers import AnnouncementParser
from menzili.scraper import MenziliScraper


class AnnnouncementScenario:
    target = "https://www.menzili.tn/"
    signin = "https://www.menzili.tn/connexion"

    def __init__(self):
        parser = AnnouncementParser

        self.login = parser.get_login("menzili")
        self.password = parser.get_password("menzili")

    def run(self):
        a = FFAgent(self.target)
        a.get_agent().implicitly_wait(10)
        s = MenziliScraper()
        print("agent started")
        self.agent = a
        a.nav(self.signin)
        a.get_by_id("old_account").click()
        a.get_by_id("email_con").send_keys(self.login)
        a.get_by_id("password").send_keys(self.password)
        a.get_by_id("btnlogin").click()
        current_url = a.get_agent().current_url

        if not current_url == "https://www.menzili.tn/acc_bord.php":
            raise Exception(
                f"Could not connect to menzili check your credentials :: (current_url: {current_url})"
            )
        a.nav("https://www.menzili.tn/deposer-une-annonce")

        s.set_cookies(a.agent.get_cookies())

        def input_value_by_name(x):
            return a.get_by_x(
                f'//form[@id="corpsconnect"]//input[@name="{x}"]'
            ).get_attribute("value")

        # Access form pre-filled data
        input_fields = ("nom", "prenom", "id_compte", "ema")
        extra_info = {field: input_value_by_name(field) for field in input_fields}
        # 2 Steps process
        res = s.create_announcement(extra_info)
        print("Menzili response HEADERS -> ", res.headers)
        print("Menizli response", res.raw)
        location = res.headers.get("location", "")
        # location = a.get_agent().current_url
        print("Found location :: ", location)
        s.confirm_announcement(location)
        a.nav("https://www.menzili.tn/acc_bord.php")
        links = a.get_by_x(
            '//section[@id="block-listing"]//a[contains(@href, "annonce") and not(@class)]',
            multiple=True,
        )
        print("Found announcements -> ", links)
        new_announcement_url = links[-1].get_attribute("href")
        a.terminate()
        return new_announcement_url
