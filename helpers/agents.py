from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from os import system, path
from random import randint

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
            print("dev & proxy")

            # TODO: Fix proxying
            proxies = {
                "proxyType": "manual",
                "httpProxy": "127.0.0.1:8000",
                "httpsProxy": "127.0.0.1:8000"
                # 'sslProxy': ''
            }

            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.http_proxy = "127.0.0.1:8000"
            prox.socks_proxy = "127.0.0.1:8000"
            prox.ssl_proxy = "127.0.0.1:8000"

            capabilities = webdriver.DesiredCapabilities.FIREFOX
            prox.add_to_capabilities(capabilities)

            # prox.socks_proxy = "ip_addr:port"
            # prox.ssl_proxy = "http://localhost:8000"

            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True

            # capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
            # capabilities['proxy'] = proxies
            # prox.add_to_capabilities(capabilities)
            # prox.add_to_capabilities({'proxy': proxies})
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
                print(self.agent.capabilities)
            except Exception as e:
                print("FAILED to create agent dev & proxy")
                print(e)
        else:
            print("NO dev & NO proxy")
            self.agent = Firefox(options=options)
        # print(self.agent.capabilities)
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
