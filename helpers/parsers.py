from helpers.validators.credentialsvalidator import CredentialsValidator


class AnnouncementParser:
    _credentials = {}
    _sites = []
    _req = None

    @classmethod
    def parse_request(cls, data):
        # self._req = json.loads(request)
        cls._req = data
        # Parse credentials here to a more useful format
        for id, cred in cls._req["credentials"].items():
            # cred = list(entry.values())[0]
            # print(cred)
            keys = list(cred.keys())
            if "_login" in keys[0]:
                website = keys[0][:-6]
                login = cred[keys[0]]
                pwd = cred[keys[1]]
            elif "_password" in keys[0]:
                website = keys[0][:-9]
                login = cred[keys[1]]
                pwd = cred[keys[0]]
            else:
                raise Exception(
                    f'[Credentials Parsing Error]: {cred} -- please check that "credentials" section is well formatted'
                )

            cls._credentials[website] = {"login": login, "password": pwd, "id": id}
            cls._sites.append(website)
        print(f"Pars: {cls._credentials}")
        print(f"Found websites in request {cls._sites}")

    @classmethod
    def get_login(cls, site):
        print("getting login", f" '{site}'")
        return cls._credentials.get(site)["login"]

    @classmethod
    def get_password(cls, site):
        print("getting pass", f" '{site}'")
        return cls._credentials.get(site)["password"]

    @classmethod
    def get_id(cls, site):
        return cls._credentials.get(site)["id"]

    @classmethod
    def run_validators(cls):
        """Runs all pre-job launch validators"""
        for site in cls._sites:
            login = cls._credentials[site]["login"]
            pwd = cls._credentials[site]["password"]
            try:
                CredentialsValidator.validate(site, login, pwd)
            except Exception as e:
                print(f"Failed to validate for {site}", " --- ", str(e))

    @classmethod
    @property
    def jobs_start_notify_target(cls):
        return cls._req["url_when_getting_data"]

    @classmethod
    @property
    def jobs_end_notify_target(cls):
        return cls._req["url_when_finish"]

    @classmethod
    @property
    def notify_access_header(cls):
        return {"X_TOKEN": cls._req["X_TOKEN"]}

    @classmethod
    @property
    def images_urls(cls):
        return [item["web_path"] for item in cls._req["property"]["images"]]

    @classmethod
    @property
    def credentials(cls):
        return cls._credentials

    @classmethod
    @property
    def property_type(cls):
        return cls._req["property"]["property_type"]["name_slug"]

    @classmethod
    @property
    def surface(cls):
        return cls._req["property"].get("surface", "")

    @classmethod
    @property
    def description(cls):
        return cls._req["property"]["description"]

    @classmethod
    @property
    def pieces(cls):
        return cls._req["property"]["pieces"]["value"]

    @classmethod
    # @property
    def governorate(cls, site):
        # TODO:
        field = f"id_{site}"
        return cls._req["property"]["gouvernorat"][field]

    @classmethod
    # @property
    def delegation(cls, site):
        # TODO:
        field = f"id_{site}"
        return cls._req["property"]["delegation"][field]

    @classmethod
    @property
    def vocation(cls):
        return cls._req["property"]["vocation"]["name"]

    @classmethod
    @property
    def baths(cls):
        return cls._req["property"].get("salle_de_bain", "")

    @classmethod
    @property
    def chambers(cls):
        return cls._req["property"]["chambres"]

    @classmethod
    @property
    def title(cls):
        return cls._req["property"]["name"]

    @classmethod
    @property
    def price(cls):
        return cls._req["property"]["prix"]

    @classmethod
    @property
    def phone(cls):
        return cls._req["property"]["phone"]


class HTMLParser:
    pass
