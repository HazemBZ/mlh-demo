from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxOptions

import tomllib

class FFAgent:
    def __init__(self, url, **kwargs):
        self.url = url
        settings = None
        self.agent = None

        try:
            with open(".env.toml", "rb") as fp:
                settings = tomllib.load(fp)
        except Exception as e:
            print(e)

        options = Options()
        options.headless = settings["headless"]
        print("headless -> ", options.headless)

        if settings["environment"] == "dev" and settings["proxy_on"] == 1:
            print("dev and proxy")

            capabilities = webdriver.DesiredCapabilities.FIREFOX

            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True

            capabilities.update(
                {
                    "acceptInsecureCerts": True,
                    "acceptSslCerts": True,
                    "assumeUntrustedIssuer": False,
                }
            )
            try:
                self.agent = Firefox(
                    firefox_profile=profile,
                    options=options,
                    desired_capabilities=capabilities,
                    capabilities=capabilities,
                    **kwargs
                )
            except Exception as e:
                print("FAILED to create agent dev & proxy")
                print(e)
        else:
            print("NO dev and NO proxy")
            """
            This to fix FF error https://stackoverflow.com/questions/46809135/webdriver-exceptionprocess-unexpectedly-closed-with-status-1 
            due to image change
            """
            opts = FirefoxOptions()
            opts.add_argument("--headless")
            self.agent = webdriver.Firefox(options=opts)
        self.agent.get(url)

    def nav(self, url):
        self.agent.get(url)

    def get_by_x(self, exp, multiple=False):
        if multiple:
            return self.agent.find_elements(By.XPATH, exp)
        return self.agent.find_element(By.XPATH, exp)

    def get_by_id(self, exp):
        return self.agent.find_element(By.ID, exp)

    def terminate(self):
        self.agent.close()

    def get_agent(self):
        return self.agent


## Experimental
def generate_interaction(selector_type, selector_target, action):
    return {
        selector_type: selector_type,
        selector_target: selector_target,
        action: action,
    }

INTERACTIONS = [
    {"selector_type": "x", "selector_target": "", "action": "click"},
]
