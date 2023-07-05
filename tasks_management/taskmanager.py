import tomllib
from tasks import create_task
from tasks import notify_post_task
from celery import chord
from helpers.parsers import AnnouncementParser
from helpers.common_requests import send_data


class TasksManager:
    _supported_sites = []

    @classmethod
    def load_configs(cls):
        settings = None
        with open("config.toml", "rb") as fp:
            settings = tomllib.load(fp)

        cls._supported_sites = settings["supported_sites"]

    @classmethod
    def run_jobs(cls, data):
        for site in cls._supported_sites:
            cls.run_job(site, data)

    @classmethod
    def run_jobs_and_notify(cls, data):
        try:
            send_data(
                AnnouncementParser.jobs_start_notify_target,
                json={
                    "X_TOKEN": AnnouncementParser.notify_access_header.get("X_TOKEN")
                },
                headers=AnnouncementParser.notify_access_header,
            )
        except Exception as e:
            print("Failed to send job start notification :: reason :: ", e)
        # TODO: Add error link in case of failure
        chord(
            (create_task.si(site=site, data=data) for site in cls._supported_sites),
            notify_post_task.s(
                AnnouncementParser.jobs_end_notify_target,
                AnnouncementParser.notify_access_header,
            ).set(link_error=["chord_error_handle"]),
        ).apply_async()

    @classmethod
    def run_job(cls, site, data):
        print("Running job for ", site)
        create_task.delay(site=site, data=data)
