from helpers.agents import FFAgent
from helpers.base_entities import BaseScraper
import requests
import warnings


class _CredentialsValidationError(Exception):
    """Exception raised when login fails

    Attributes:
        site -- the website tested for login
        message -- error message template
    """

    def __init__(self, site, message='Failed login process for website "$1" '):
        self.site = site
        self.message = message.replace("$1", self.site)
        super().__init__(self.message)


class MenziliValidator:
    _target = "https://www.menzili.tn/connexion"
    _name = "Menzili"

    @classmethod
    def run(cls, login, password):
        f_data = {"email_con": login, "password": password, "checked_old_acc": "1"}
        res = requests.post(cls._target, data=f_data, allow_redirects=False)

        LOCATION = "acc_bord.php"
        valid = res.headers.get("location", "") == LOCATION

        if not valid:
            raise _CredentialsValidationError(cls._name)


class CavatnValidator:
    _target = "https://www.cava.tn/site/getuserbyemail/"
    _name = "Cava"

    @classmethod
    def run(cls, login, password):
        try:
            a = FFAgent("https://www.cava.tn/")
        except Exception as e:
            print("Failed to start agent for  Cavatan", " --- ", str(e))
            return
        else:
            a.get_by_x('//a[@data-target="#login-modal"]').click()
            csrf = a.get_by_x('//input[@name="_csrf-frontend"]').get_attribute("value")
            print(type(csrf))
            data = {
                "email": login,
                "password": password,
                "_csrf-frontend": csrf,
            }
            s = BaseScraper()
            s.set_cookies(a.get_agent().get_cookies())
            resp = s.session.post(cls._target, data=data)
            a.terminate()
            load = resp.text
            valid = "user" in load
            if not valid:
                raise _CredentialsValidationError(cls._name)


class CredentialsValidator:
    _validators = {
        "cava": CavatnValidator,
        "menzili": MenziliValidator,
    }

    @classmethod
    def validate(cls, site, login, password):
        if site in cls._validators:
            cls._validators[site].run(login, password)
        else:
            warnings.warn(f"{site}'s Validator not implemented yet")
