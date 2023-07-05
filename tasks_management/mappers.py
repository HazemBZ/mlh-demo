import warnings

from cavatn.scenarios import \
    AnnnouncementScenario as CavatnAnnnouncementScenario
from menzili.scenarios import \
    AnnnouncementScenario as MenziliAnnouncementScenario


class Unsupported:
    def run(self):
        print("Unsupported site scenario ran ")


class ScenariosMapper:
    __map = {
        "cava": CavatnAnnnouncementScenario,
        "menzili": MenziliAnnouncementScenario,
        "unsupported": Unsupported,
    }

    @classmethod
    def get_scenario(cls, site):
        if site in cls.__map:
            print(f"Found scenario for {site}")
            return cls.__map.get(site)
        else:
            warnings.warn(f'No scenarios for "{site}" yet')
            return Unsupported
